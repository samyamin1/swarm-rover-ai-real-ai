from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='swarm_agents',
            executable='alpha_agent',
            name='alpha_agent',
            output='screen',
            emulate_tty=True,
            arguments=['--ros-args', '--log-level', 'info']
        ),
        Node(
            package='swarm_agents',
            executable='agent_node',
            name='agent_node_1',
            output='screen',
            emulate_tty=True,
            arguments=['--ros-args', '--log-level', 'info']
        ),
        Node(
            package='swarm_agents',
            executable='agent_node',
            name='agent_node_2',
            output='screen',
            emulate_tty=True,
            arguments=['--ros-args', '--log-level', 'info']
        ),
        Node(
            package='swarm_agents',
            executable='agent_node',
            name='agent_node_3',
            output='screen',
            emulate_tty=True,
            arguments=['--ros-args', '--log-level', 'info']
        ),
        Node(
            package='swarm_agents',
            executable='agent_node',
            name='agent_node_4',
            output='screen',
            emulate_tty=True,
            arguments=['--ros-args', '--log-level', 'info']
        ),
        Node(
            package='swarm_agents',
            executable='agent_node',
            name='agent_node_5',
            output='screen',
            emulate_tty=True,
            arguments=['--ros-args', '--log-level', 'info']
        ),
    ])
