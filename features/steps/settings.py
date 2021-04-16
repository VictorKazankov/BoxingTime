from behave import given, when, then


@given('Open settings screen')
def is_displayed_settings_screen(context):
    context.app.settings_screen.open()


@when('Tap right button training option')
def tap_right_button_training_option(context):
    context.app.settings_screen.tab_right_button_training_time_option()


@when('Tap left button training option')
def tap_left_button_training_option(context):
    context.app.settings_screen.tab_left_button_training_time_option()


@when('Change slider sound settings')
def move_slider_sound_settings(context):
    context.app.settings_screen.move_slider_sound_settings()


@then('Training time increase 10')
def training_time_should_be_increase_10_sec(context):
    context.app.settings_screen.training_time_should_be_increase_10_sec()


@then('Training time decrease 10')
def training_time_should_be_decrease_10_sec(context):
    context.app.settings_screen.training_time_should_be_decrease_10_sec()


@then('Slider state should be changed')
def slider_should_be_changed(context):
    context.app.settings_screen.is_changed_sound_slider()
