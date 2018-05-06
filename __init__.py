# coding: utf-8

from fabkit import *  # noqa
from fablib.base import SimpleBase


class Vpp(SimpleBase):
    def __init__(self):
        self.packages = {
            # 'Ubuntu .*': ['make', 'dpdk', 'dpdk-dev', 'dpdk-doc', 'libdpdk-dev']
            'Ubuntu .*': ['make', 'gcc', 'libnuma-dev', 'numactl']
        }

        self.services = {
            'Ubuntu .*': ['vpp']
        }

    def setup(self):
        self.init()
        self.reserve_hugepages()
        sudo('apt-get update')
        self.install_packages()

        if not filer.exists('dpdk-17.11.1.tar.xz'):
            run('wget https://fast.dpdk.org/rel/dpdk-17.11.1.tar.xz')
        if not filer.exists('dpdk-stable-17.11.1'):
            run('tar xf dpdk-17.11.1.tar.xz')

        with api.warn_only():
            result = run('lsmod | grep igb_uio')
            if result.return_code != 0:
                with api.cd('dpdk-stable-17.11.1'):
                    run('make install T=x86_64-native-linuxapp-gcc')
                    sudo('modprobe uio')
                    sudo('insmod x86_64-native-linuxapp-gcc/kmod/igb_uio.ko')

        if not filer.exists('vpp'):
            run('git clone https://gerrit.fd.io/r/vpp')
            sudo('./vpp/extras/vagrant/build.sh')
            sudo('dpkg -i build-root/*.deb')

        self.enable_services().start_services()

    def reserve_hugepages(self):
        sudo('echo 512 > /sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages')
        filer.mkdir('/mnt/huge')
        sudo('mount -t hugetlbfs nodev /mnt/huge')
