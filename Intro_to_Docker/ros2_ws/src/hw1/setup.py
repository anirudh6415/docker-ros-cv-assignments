from setuptools import setup

package_name = 'hw1'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'parta_circle = hw1.draw_circle:main',
            'partb_talker = hw1.publisher_member_function:main',
            'partb_listener = hw1.subscriber_member_function:main',
            'partc_pub_name = hw1.publisher_name:main',
            'partc_pub_count = hw1.publisher_count:main',
            'partc_sub_all = hw1.subscriber_all:main',
        ],
    },
)
