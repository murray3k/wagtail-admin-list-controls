from django.test import RequestFactory
from django_webtest import WebTest
from admin_list_controls.filters import BaseFilter, TextFilter, BooleanFilter, ChoiceFilter, \
    MultipleChoiceFilter, RadioFilter


class TestControls(WebTest):
    def setUp(self):
        self.factory = RequestFactory()

    def test_base_filter(self):
        filter_ = BaseFilter(
            name='test_name',
            label='test_label',
        )
        filter_.prepare(self.factory.get('/?test_name=test_value'))
        self.assertEqual(filter_.cleaned_value, 'test_value')
        self.assertEqual(
            filter_.serialize(),
            {
                'object_type': 'filter',
                'children': [],
                'filter_type': '',
                'name': 'test_name',
                'label': 'test_label',
                'value': 'test_value',
            },
        )

    def test_base_filter_with_default_value(self):
        filter_ = BaseFilter(
            name='test_name',
            label='test_label',
            default_value='test_default_value',
        )
        filter_.prepare(self.factory.get('/'))
        self.assertEqual(filter_.cleaned_value, 'test_default_value')
        filter_.prepare(self.factory.get('/?test_name'))
        self.assertEqual(filter_.cleaned_value, '')
        filter_.prepare(self.factory.get('/?test_name=test_value'))
        self.assertEqual(filter_.cleaned_value, 'test_value')

    def test_text_filter_value(self):
        filter_ = TextFilter(
            name='test_name',
            label='test_label',
        )
        filter_.prepare(self.factory.get('/'))
        self.assertEqual(filter_.cleaned_value, '')
        filter_.prepare(self.factory.get('/?test_name='))
        self.assertEqual(filter_.cleaned_value, '')
        filter_.prepare(self.factory.get('/?test_name=test_value'))
        self.assertEqual(filter_.cleaned_value, 'test_value')

    def test_boolean_filter_value(self):
        filter_ = BooleanFilter(
            name='test_name',
            label='test_label',
        )
        filter_.prepare(self.factory.get('/'))
        self.assertEqual(filter_.cleaned_value, False)
        filter_.prepare(self.factory.get('/?test_name='))
        self.assertEqual(filter_.cleaned_value, False)
        filter_.prepare(self.factory.get('/?test_name=something'))
        self.assertEqual(filter_.cleaned_value, True)

    def test_radio_filter_value(self):
        filter_ = RadioFilter(
            name='test_name',
            label='test_label',
            choices=(
                ('foo', 'Foo'),
                ('bar', 'Bar'),
            )
        )
        filter_.prepare(self.factory.get('/'))
        self.assertEqual(filter_.cleaned_value, None)
        filter_.prepare(self.factory.get('/?test_name='))
        self.assertEqual(filter_.cleaned_value, None)
        filter_.prepare(self.factory.get('/?test_name=woz'))
        self.assertEqual(filter_.cleaned_value, None)
        filter_.prepare(self.factory.get('/?test_name=foo'))
        self.assertEqual(filter_.cleaned_value, 'foo')

    def test_choice_filter_value(self):
        filter_ = ChoiceFilter(
            name='test_name',
            label='test_label',
            choices=(
                ('foo', 'Foo'),
                ('bar', 'Bar'),
            )
        )
        filter_.prepare(self.factory.get('/'))
        self.assertEqual(filter_.cleaned_value, None)
        filter_.prepare(self.factory.get('/?test_name='))
        self.assertEqual(filter_.cleaned_value, None)
        filter_.prepare(self.factory.get('/?test_name=woz'))
        self.assertEqual(filter_.cleaned_value, None)
        filter_.prepare(self.factory.get('/?test_name=foo'))
        self.assertEqual(filter_.cleaned_value, 'foo')

    def test_multiple_choice_filter_value(self):
        filter_ = MultipleChoiceFilter(
            name='test_name',
            label='test_label',
            choices=(
                ('foo', 'Foo'),
                ('bar', 'Bar'),
            )
        )
        filter_.prepare(self.factory.get('/'))
        self.assertEqual(filter_.cleaned_value, [])
        filter_.prepare(self.factory.get('/?test_name='))
        self.assertEqual(filter_.cleaned_value, [])
        filter_.prepare(self.factory.get('/?test_name=woz'))
        self.assertEqual(filter_.cleaned_value, [])
        filter_.prepare(self.factory.get('/?test_name=foo'))
        self.assertEqual(filter_.cleaned_value, ['foo'])
        filter_.prepare(self.factory.get('/?test_name=foo&test_name=foo'))
        self.assertEqual(filter_.cleaned_value, ['foo', 'foo'])
        filter_.prepare(self.factory.get('/?test_name=foo&test_name=bar'))
        self.assertEqual(filter_.cleaned_value, ['foo', 'bar'])
        filter_.prepare(self.factory.get('/?test_name=foo&test_name=bar&test_name=woz'))
        self.assertEqual(filter_.cleaned_value, ['foo', 'bar'])
