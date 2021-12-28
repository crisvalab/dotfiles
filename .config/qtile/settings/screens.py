from libqtile.config import Screen
from libqtile import bar
# from .monitors import connected_monitors
from .widgets import primary_widgets
# import subprocess


def status_bar(widgets, bar_size=40, opacity=0.92):
    return bar.Bar(widgets, bar_size, opacity=opacity)


screens = [Screen(top=status_bar(primary_widgets))]


# if connected_monitors > 1:
#     subprocess.run(
#         '/home/cristian/.screenlayout/external-monitor.sh; xrdb -merge <(echo "Xft.dpi: 96")',
#         shell=True,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#     )
#     screens = [Screen(top=status_bar(primary_widgets, 18))]
# else:
#     subprocess.run(
#         '/home/cristian/.screenlayout/default; xrdb -merge <(echo "Xft.dpi: 193")',
#         shell=True,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#     )



    # for _ in range(1, connected_monitors):
    #     screens.append(Screen(top=status_bar(secondary_widgets)))
