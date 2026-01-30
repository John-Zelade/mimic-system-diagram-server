from django.db import models
import uuid
# Create your models here.
class Diagram(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DiagramNode(models.Model):
    NODE_TYPES = [
        ("area", "Area"),
        ("zone", "Zone"),
        ("rect", "Rectangle"),
        ("tank", "Tank"),
        ("water-pump", "Water Pump"),
        ("pipe", "Pipe"),
        ("meter", "Meter"),
        ("sprinkler", "Sprinkler"),
        ("isolation-valve", "Isolation Valve"),
        ("control-valve", "Control Valve"),
        ("motor", "Motor"),
        ("circle", "Circle"),
        ("ellipse", "Ellipse"),
        ("capsule", "Capsule"),
        ("cylinder", "Cylinder"),
        ("text", "Text"),
        ("custom", "Custom"),
        ("tee", "Tee"),
        ("cross", "Cross"),
        ("level-transmitter", "Level Transmitter"),
        ("soil-moisture-sensor", "Soil Moisture Sensor"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    diagram = models.ForeignKey(Diagram, on_delete=models.CASCADE, related_name="nodes")

    type = models.CharField(max_length=50, choices=NODE_TYPES)

    x = models.FloatField()
    y = models.FloatField()
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)

    rotation = models.FloatField(null=True, blank=True)
    scale_x = models.FloatField(null=True, blank=True)
    scale_y = models.FloatField(null=True, blank=True)

    fill = models.CharField(max_length=50, null=True, blank=True)
    stroke = models.CharField(max_length=50, null=True, blank=True)
    stroke_width = models.FloatField(null=True, blank=True)
    opacity = models.FloatField(null=True, blank=True)

    draggable = models.BooleanField(default=True)
    locked = models.BooleanField(default=False)
    selectable = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)
    resizable = models.BooleanField(default=True)
    connectable= models.BooleanField(default=True)
    z_index = models.IntegerField(default=0)
    group_id = models.UUIDField(null=True, blank=True)

    # JSON fields (perfect for styles & runtime data)
    style = models.JSONField(null=True, blank=True)
    properties = models.JSONField(null=True, blank=True)
    data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.type} ({self.id})"

class DiagramNodePort(models.Model):
    PORT_TYPES = [
        ("in", "In"),
        ("out", "Out"),
        ("both", "Both"),
    ]
    PORT_POSITIONS = [
        ("top", "Top"),
        ("right", "Right"),
        ("bottom", "Bottom"),
        ("left", "Left"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    node = models.ForeignKey(DiagramNode, on_delete=models.CASCADE, related_name="ports")

    x = models.FloatField()
    y = models.FloatField()
    type = models.CharField(max_length=10, choices=PORT_TYPES, default="both")
    position = models.CharField(max_length=10, choices=PORT_POSITIONS,default="left")

    def __str__(self):
        return f"Port {self.id}"

class DiagramLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    diagram = models.ForeignKey(Diagram, on_delete=models.CASCADE, related_name="links")

    label = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=20, default="line")

    points = models.JSONField()  # number[]

    def __str__(self):
        return f"Link {self.id}"

class DiagramLinkEndpoint(models.Model):
    ENDPOINT_ROLE = [
        ("from", "From"),
        ("to", "To"),
    ]

    link = models.ForeignKey(DiagramLink, on_delete=models.CASCADE, related_name="endpoints")
    role = models.CharField(max_length=10, choices=ENDPOINT_ROLE)

    node = models.ForeignKey(DiagramNode, on_delete=models.CASCADE)
    port = models.ForeignKey(
        DiagramNodePort,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
