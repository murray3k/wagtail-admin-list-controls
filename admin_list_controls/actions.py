class BaseAction:
    object_type = 'action'
    action_type = ''

    def serialize(self):
        return {
            'object_type': self.object_type,
            'action_type': self.action_type,
        }


class SetValue(BaseAction):
    action_type = 'set_value'

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def serialize(self):
        return dict(super().serialize(), **{
            'name': self.name,
            'value': self.value,
        })


class AppendValue(BaseAction):
    action_type = 'append_value'

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def serialize(self):
        return dict(super().serialize(), **{
            'name': self.name,
            'value': self.value,
        })


class RemoveValue(BaseAction):
    action_type = 'remove_value'

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def serialize(self):
        return dict(super().serialize(), **{
            'name': self.name,
            'value': self.value,
        })


class Link(BaseAction):
    action_type = 'link'

    def __init__(self, url):
        self.url = url

    def serialize(self):
        return dict(super().serialize(), **{
            'url': self.url,
        })


class TogglePanel(BaseAction):
    action_type = 'toggle_panel'
    show_panel_toggle_icon = True

    def __init__(self, ref):
        self.ref = ref

    def serialize(self):
        return dict(super().serialize(), **{
            'ref': self.ref,
            'show_panel_toggle_icon': self.show_panel_toggle_icon,
        })


class SubmitForm(BaseAction):
    action_type = 'submit_form'
