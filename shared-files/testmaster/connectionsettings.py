# This is the connection settings file for local Katana builds

from buildbot.status import html, status_push, status_nats
from buildbot.status.web import authz, auth


USER = "myuser"
PASSWORD = "mypassword"
DATABASE = "katana-dev"
HOST = "localhost"
HTTP_PORT = 8001


def get_slave_port():
    """
    Gets the port that slaves should connect to
    """
    return 9901


def get_all_slaves():
    """
    Appends locally created slaves to the list "slaves" and "friendly_slaves".
    If none exist, returns without performing a function.
    """
    """
    DEFAULT SLAVE GROUPS:
        'all_lin_slaves',
        'all_mac_slaves',
        'all_windows_slaves',
        'lin_general_slaves',
        'lin_hg_slaves',
        'lin_node_slaves',
        'mac_10.10_general_slaves',
        'mac_android_slaves',
        'mac_general_slaves',
        'mac_gfxmetal_intel',
        'mac_gfxmetal_nvidia',
        'mac_gfx_test_slaves',
        'mac_gfx_webgl2',
        'mac_intel_android_slaves',
        'mac_ios7_metal_slaves',
        'mac_ios7_slaves',
        'mac_ios7_slaves_with_device',
        'mac_ios7_slaves_with_gles2_device',
        'mac_ios7_slaves_with_gles3_device',
        'mac_ios_slaves',
        'mac_ios_slaves_with_arm64_device',
        'mac_ipad_mini_2_slaves',
        'mac_shield_slaves',
        'mac_tvos_slaves',
        'osx_perf_minions',
        'win10_general_slaves',
        'win10_gfx_test_slaves',
        'win7_general_slaves',
        'win7_linuxtest_slaves',
        'win7_ps3_slaves',
        'win7_psp_slaves',
        'win7_vs2012_slaves',
        'win7_wiiu_slaves',
        'win7_xbox_slaves',
        'win8.1_general_slaves',
        'win8.1_wp80_slaves',
        'win8.1_wp8_slaves',
        'win81slaves_fmod',
        'win_gfx_test',
        'win_perf_minions',
        'win_ps4_slaves',
        'win_xboxone_slaves'
    """
    # Get our slaves from Yumi
    import yumimanager, socket
    from pymysql.err import OperationalError
    try:
        reload(yumimanager)
        slaves = yumimanager.getAgentDict("10.45.4.98")
        friendly_slaves = yumimanager.getAgentDict("10.45.4.98", True)
    except OperationalError:
        # Failed to establish a connection to Yumi.
        slaves = {}
        friendly_slaves = {}

        friendly_slaves['no_slave'] = [{'id': -1, 'name': 'Not Available', 'friendlyName': 'Not Available', 'os': 'N/A'}]

        friendly_slaves['lin_hg_slaves'] = []
        friendly_slaves['lin_general_slaves'] = []
        friendly_slaves['all_lin_slaves'] = []
        slaves['lin_hg_slaves'] = []
        slaves['lin_general_slaves'] = []
        slaves['all_lin_slaves'] = []

    slave_1 = {'friendlyName': 'build-slave-01', 'os': 'Linux', 'id': 200, 'name': 'build-slave-01'}
    slaves['lin_hg_slaves'].append('build-slave-01')
    friendly_slaves['lin_hg_slaves'].append(slave_1)
    slaves['all_lin_slaves'].append('build-slave-01')
    friendly_slaves['all_lin_slaves'].append(slave_1)

    slave_2 = {'friendlyName': 'build-slave-02', 'os': 'Linux', 'id': 201, 'name': 'build-slave-02'}
    slaves['lin_general_slaves'].append('build-slave-02')
    friendly_slaves['lin_general_slaves'].append(slave_2)
    slaves['all_lin_slaves'].append('build-slave-02')
    friendly_slaves['all_lin_slaves'].append(slave_2)

    return slaves, friendly_slaves


def get_buildbot_url():
    """
    Gets the URL that users can connect to.
    """
    return "http://10.45.4.98:8001/"


def get_database_url():
    """
    Gets the URL (as a touple) that the server uses to connect to the database.
    """
    details = {
        # This specifies what database buildbot uses to store its state.  You can leave
        # this at its default for all but the largest installations.
        'db_url': "mysql+pymysql://{user}:{password}@{host}/{database}?max_idle=300".format(
            user=USER, password=PASSWORD,
            database=DATABASE, host=HOST
        ),
        'db_poll_interval': 6,
    }
    return details



def get_realtime_server_url():
    """
    Returns the URL that the realtime server (eg: autobahn) is running on
    """
    return "ws://localhost:8010/ws"


def mysql_database():
    """
    Gets the MySQL database containing the Katana builds.
    """
    return DATABASE

