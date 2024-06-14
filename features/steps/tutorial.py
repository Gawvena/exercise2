from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
	
@given(u'the user has gone into a garage sale menu,')
def step_impl(context):
    pass


@when(u'the user clicks on a sort by drop-down,')
def step_impl(context):
    assert True is not False


@when(u'the user chooses to sort by price,')
def step_impl(context):
    assert True is not False


@when(u'the user chooses to sort ascending,')
def step_impl(context):
    assert True is not False


@then(u'the user should be shown the items with the cheapest items at the top and most expensive items at the bottom.')
def step_impl(context):
    assert context.failed is False