from setuptools import find_packages, setup

package_name = 'prius_sdk_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='stas',
    maintainer_email='stas.kolodziejczyk@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "video_recorder=prius_sdk_pkg.video_recorder:main",
            "driving_node=prius_sdk_pkg.driving_node:main",
            "computer_vision_node=prius_sdk_pkg.computer_vision_node:main",
            "sdf_spawner=prius_sdk_pkg.sdf_spawner:main",
        ],
    },
)
