"""Tables for Circuit Maintenance."""
import django_tables2 as tables
from django_tables2.utils import Accessor

from nautobot.utilities.tables import BaseTable, ToggleColumn

from .models import CircuitMaintenance, RawNotification, CircuitImpact, EmailSettings, Note


class CircuitMaintenanceTable(BaseTable):
    """Table to display maintenace model."""

    name = tables.LinkColumn(viewname="plugins:nautobot_circuit_maintenance:circuitmaintenance", args=[Accessor("id")])

    pk = ToggleColumn()

    class Meta(BaseTable.Meta):
        """Meta for class CircuitMaintenanceTable."""

        model = CircuitMaintenance
        fields = ("pk", "ack", "name", "status", "start_time", "end_time")


class RawNotificationTable(BaseTable):
    """Table to display Raw Notifications model."""

    subject = tables.LinkColumn(viewname="plugins:nautobot_circuit_maintenance:rawnotification", args=[Accessor("id")])

    pk = ToggleColumn()

    class Meta(BaseTable.Meta):
        """Meta for class CircuitMaintenanceNofiticationRawTable."""

        model = RawNotification
        fields = ("pk", "subject", "provider", "sender", "source", "parsed", "date")


class CircuitImpactTable(BaseTable):
    """Table to display Circuit Impact model."""

    pk = ToggleColumn()

    class Meta(BaseTable.Meta):
        """Meta for class CircuitImpactTable."""

        model = CircuitImpact
        fields = ("pk", "level", "maintenance", "circuit", "impact")


class NoteTable(BaseTable):
    """Table to display Note model."""

    pk = ToggleColumn()

    class Meta(BaseTable.Meta):
        """Meta for class NoteTable."""

        model = Note
        fields = ("pk", "maintenance", "title", "level", "comment", "date")


class EmailSettingsTable(BaseTable):
    """Table to display Circuit Impact model."""

    email = tables.LinkColumn(viewname="plugins:nautobot_circuit_maintenance:emailsettings_edit", args=[Accessor("id")])

    pk = ToggleColumn()

    class Meta(BaseTable.Meta):
        """Meta for class CircuitImpactTable."""

        model = EmailSettings
        fields = ("pk", "email", "url", "server_type", "providers")
