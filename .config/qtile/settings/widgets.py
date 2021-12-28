from libqtile import widget
from .theme import colors
from .batterywidget import Battery
from .monitors import connected_monitors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

config_parameters = {
    "widgets_font_size": 30,
    "icon_font_size": 24,
    "window_name_font_size": 26,
    "powerline_font_size": 60,
    "systray_icon_size": 35,
    "widget_defaults_font_size": 25
}

if connected_monitors > 1:
    for param in config_parameters:
        config_parameters[param] = int(config_parameters[param]/2)


def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=config_parameters['icon_font_size'], text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",
        fontsize=config_parameters['powerline_font_size'],
        padding=-4
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=config_parameters['widgets_font_size'],
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=config_parameters['window_name_font_size'], padding=10),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),
    # icon(bg="color4", text='  '),
    # widget.Memory(
    #     **base(bg='color4'),
    #     format='{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm}'
    # ),
    # icon(bg="color4", text=' '),
    # icon(bg="color4", text='  '), # Icon: nf-fa-download
    # widget.CheckUpdates(
    #     background=colors['color4'],
    #     colour_have_updates=colors['text'],
    #     colour_no_updates=colors['text'],
    #     no_update_string='0',
    #     display_format=' {updates}',
    #     update_interval=1800,
    #     custom_command='checkupdates',
    # ),
    icon(bg="color4", text=' 墳 '),
    widget.Volume(**base(bg='color4')),
    icon(bg="color4", text=' '),

    powerline('color3', 'color4'),
    # icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    # widget.Net(**base(bg='color3'), interface='wlp0s20f3', format='{interface}: ↓{down} ↑{up} '),
    Battery(
        **base(bg='color3'),
        show_short_text=False,
        format='{char} {percent:2.0%} {hour:d}:{min:02d} ',
        update_interval=3
    ),

    powerline('color2', 'color3'),
    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color2'),
    icon(bg="color1", text='  '), # Icon: nf-mdi-calendar_clock
    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color1'),
    widget.Systray(background=colors['dark'], padding=5, icon_size=config_parameters['systray_icon_size']),

    separator(),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': config_parameters['widget_defaults_font_size'],
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
