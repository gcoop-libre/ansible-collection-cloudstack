#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2024, Cristian G. Segarra <cristian@segarra.com.ar>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = '''
---
module: cs_k8s
short_description: Manages Kubernetes clusters on Apache CloudStack based clouds.
description:
    - Create, update and remove clusters.
author: Cristian G. Segarra (@csegarra)
version_added: 2.3.0
options:
  account:
    description:
      - An optional account for the virtual machines.
      - Required if I(domain!=null).
    type: str
  control_nodes:
    description:
      - Number of Kubernetes cluster control nodes, default is 1.
    type: int
  description:
    description:
      - Description for the Kubernetes cluster.
      - Required if I(state=present)
    type: str
  docker_registry:
    description:
      - Docker image private registry info.
    type: dict
    suboptions:
      url:
        description:
          - URL for the docker image private registry.
        type: str
      username:
        description:
          - User name for the docker image private registry.
        type: str
      password:
        description:
          - Password for the docker image private registry.
        type: str
  domain:
    description:
      - The domain for the virtual machine.
      - Required if I(account!=null).
    type: str
  load_balancer:
    description:
      - External load balancer IP address while using shared network with Kubernetes HA cluster.
    type: str
  name:
    description:
      - Name for the Kubernetes cluster.
    type: str
    required: true
  network:
    description:
      - The network in which Kubernetes cluster is to be launched.
    type: str
  poll_async:
    description:
      - Poll async jobs until job has finished.
    type: bool
    default: yes
  project:
    description:
      - Deploy cluster for the project.
    type: str
  root_disk:
    description:
      - Root disk size in GB for each node.
    type: int
  service_offering:
    description:
      - The service offering for the virtual machines in the cluster.
      - Required if I(state=present)
    type: str
  size:
    description:
      - Number of Kubernetes cluster worker nodes.
      - Required if I(state=present)
    type: int
  ssh_key:
    description:
      - Name of the ssh key pair used to login to the virtual machines.
    type: str
  state:
    description:
      - State of the Kubernetes cluster.
    type: str
    choices: [ present, absent, disabled, enabled ]
    default: present
  version:
    description:
      - The Kubernetes version with which cluster to be launched.
      - Required if I(state=present)
    type: str
  zone:
    description:
      - Availability zone in which Kubernetes cluster to be launched.
    type: str
    required: true
extends_documentation_fragment:
- ngine_io.cloudstack.cloudstack
'''

EXAMPLES = '''
- name: Ensure a Kubernetes cluster is present
  ngine_io.cloudstack.cs_k8s:
    name: k8s-cluster-01
    description: Kubernetes cluster
    zone: ch-zrh-ix-01
    service_offering: CH23
    version: v1.27.3
    size: 4

- name: Ensure a Kubernetes cluster is disabled
  ngine_io.cloudstack.cs_k8s:
    name: k8s-cluster-01
    zone: ch-zrh-ix-01
    state: disabled

- name: Ensure a Kubernetes cluster is enabled
  ngine_io.cloudstack.cs_k8s:
    name: k8s-cluster-01
    zone: ch-zrh-ix-01
    state: enabled

- name: Ensure a Kubernetes cluster is absent
  ngine_io.cloudstack.cs_k8s:
    name: k8s-cluster-01
    zone: ch-zrh-ix-01
    state: absent
'''

RETURN = '''
---
account:
  description: The account associated with the Kubernetes cluster.
  returned: success
  type: str
  sample: Demo
autoscaling:
  description: Whether autoscaling is enabled for the cluster.
  returned: success
  type: str
  sample: Enabled
config:
  description: Kubernetes cluster config.
  returned: success
  type: str
  sample: |
    apiVersion: v1
    clusters:
    - cluster:
        certificate-authority-data: <ca-data-here>
        server: https://your-k8s-cluster.com
      name: <cluster-name>
    contexts:
    - context:
        cluster:  <cluster-name>
        user:  <cluster-name-user>
      name:  <cluster-name>
    current-context:  <cluster-name>
    kind: Config
    preferences: {}
    users:
    - name:  <cluster-name-user>
      user:
        token: <secret-token-here>
console:
  description: URL end point for the Kubernetes cluster dashboard UI.
  returned: success
  type: str
  sample: https://123.123.123.123:1234
control_nodes:
  description: The control nodes count for the Kubernetes cluster.
  returned: success
  type: int
  sample: 2
cpu:
  description: The cpu cores of the Kubernetes cluster.
  returned: success
  type: int
  sample: 4
created:
  description: The date when this Kubernetes cluster was created.
  returned: success
  type: str
  sample: 2024-01-01 00:00:00
description:
  description: The description of the Kubernetes cluster.
  returned: success
  type: str
  sample: k8s for testing
domain:
  description: The name of the domain in which the Kubernetes cluster exists.
  returned: success
  type: str
  sample: TestDomain
domain_id:
  description: The ID of the domain in which the Kubernetes cluster exists.
  returned: success
  type: str
  sample: 173f60ff-4a99-44f2-8693-023206f6f55b
endpoint:
  description: URL end point for the Kubernetes cluster.
  returned: success
  type: str
  sample: https://123.123.123.123:12345
id:
  description: UUID of the Kubernetes cluster.
  returned: success
  type: str
  sample: 04589590-ac63-4ffc-93f5-b698b8ac38b6
ip:
  description: Public IP Address of the cluster.
  returned: success
  type: str
  sample: 123.123.123.123
ip_id:
  description: Public IP Address ID of the cluster.
  returned: success
  type: str
  sample: e8e92a47-47be-47ae-b534-01a9530c52b6
max_size:
  description: Maximum size of the cluster.
  returned: success
  type: int
  sample: 10
memory:
  description: The memory the Kubernetes cluster.
  returned: success
  type: str
  sample: 16384
minsize:
  description: Minimum size of the cluster.
  returned: success
  type: int
  sample: 4
name:
  description: The name of the Kubernetes cluster.
  returned: success
  type: str
  sample: k8s-cluster-01
network:
  description: The name of the network of the Kubernetes cluster.
  returned: success
  type: str
  sample: k8s-network
network_id:
  description: The ID of the network of the Kubernetes cluster.
  returned: success
  type: str
  sample: 08738207-0319-405b-bb85-9bb4fc33d3b4
project:
  description: The project name of the Kubernetes cluster.
  returned: success
  type: str
  sample: Testing Project
project_id:
  description: The project ID of the Kubernetes cluster.
  returned: success
  type: str
  sample: 3ccb8b73-425f-4160-a0d7-471854e4855a
service_offering:
  description: The name of the service offering of the Kubernetes cluster.
  returned: success
  type: str
  sample: CH23
service_offering_id:
  description: The ID of the service offering of the Kubernetes cluster.
  returned: success
  type: str
  sample: 779410b0-0fb5-406f-9d9a-dedb7af1d5d8
size:
  description: The size (worker nodes count) of the Kubernetes cluster.
  returned: success
  type: int
  sample: 4
ssh_key:
  description: Keypair details.
  returned: success
  type: str
  sample: Testing key
state:
  description: The state of the Kubernetes cluster.
  returned: success
  type: str
  sample: Enabled
template_id:
  description: The ID of the template of the Kubernetes cluster.
  returned: success
  type: str
  sample: fc5ff8ed-32c0-4ae7-b90b-49fa314c5a29
version:
  description: The name of the Kubernetes version for the Kubernetes cluster.
  returned: success
  type: str
  sample: v1.27.3
version_id:
  description: The ID of the Kubernetes version for the Kubernetes cluster.
  returned: success
  type: str
  sample: 12d0cffb-1909-4ed3-9442-e42d68d3b702
vms:
  description: The list of virtualmachine associated with this Kubernetes cluster.
  returned: success
  type: list
  sample:
    - k8s-cluster-01-vm-01
    - k8s-cluster-01-vm-02
    - k8s-cluster-01-vm-03
    - k8s-cluster-01-vm-04
zone:
  description: The name of the zone of the Kubernetes cluster.
  returned: success
  type: str
  sample: ch-zrh-ix-01
zone_id:
  description: The ID of the zone of the Kubernetes cluster.
  returned: success
  type: str
  sample: 6f1d0efa-3d34-4b7f-861f-4d3a93ef22f5
'''

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.cloudstack import (
    AnsibleCloudStack,
    cs_argument_spec,
    cs_required_together,
)


class AnsibleCloudStackKubernetes(AnsibleCloudStack):

    def __init__(self, module):
        super(AnsibleCloudStackKubernetes, self).__init__(module)

        self.returns = {
            'associatednetworkname': 'network',
            'autoscalingenabled': 'autoscaling',
            'config': 'config',
            'consoleendpoint': 'console',
            'controlnodes': 'control_nodes',
            'cpunumber': 'cpu',
            'domainid': 'domain_id',
            'ipaddress': 'ip',
            'ipaddressid': 'ip_id',
            'keypair': 'ssh_key',
            'kubernetesversionid': 'version_id',
            'kubernetesversionname': 'version',
            'networkid': 'network_id',
            'projectid': 'project_id',
            'serviceofferingid': 'service_offering_id',
            'serviceofferingname': 'service_offering',
            'templateid': 'template_id',
            'virtualmachines': 'vms',
            'zoneid': 'zone_id',
        }
        self.k8s = None
        self.version = None
        self.service_offering = None

    def get_version(self, key=None):
        if self.version:
            return self._get_by_key(key, self.version)

        version = self.module.params.get('version')
        versions = self.query_api('listKubernetesSupportedVersions')

        if not versions:
            self.fail_json(msg='No Kubernetes versions available. Please create a version first')

        if versions:
            for v in versions['kubernetessupportedversion']:
                if version.lower() in [v['name'].lower(), v['id']]:
                    self.result['version'] = v['name']
                    self.version = v
                    return self._get_by_key(key, self.version)
        self.fail_json(msg="version '%s' not found" % version)

    def get_service_offering(self, key=None):
        if self.service_offering:
            return self._get_by_key(key, self.service_offering)

        service_offering = self.module.params.get('service_offering')
        service_offerings = self.query_api('listServiceOfferings')

        if not service_offerings:
            self.fail_json(msg='No service offerings available. Please create a service offering first')

        if service_offerings:
            for o in service_offerings['serviceoffering']:
                if service_offering.lower() in [o['name'].lower(), o['id']]:
                    self.result['service_offering'] = o['name']
                    self.service_offering = o
                    return self._get_by_key(key, self.service_offering)
        self.fail_json(msg="service offering '%s' not found" % service_offering)

    def get_k8s(self):
        if not self.k8s:
            args = {}

            uuid = self.module.params.get('id')
            if uuid:
                args['id'] = uuid
                k8s = self.query_api('listKubernetesClusters', **args)
                if k8s:
                    self.k8s = k8s['kubernetescluster'][0]
                    return self.k8s

            args['name'] = self.module.params.get('name')
            k8s = self.query_api('listKubernetesClusters', **args)
            if k8s:
                self.k8s = k8s['kubernetescluster'][0]

        return self.k8s

    def present_k8s(self):
        k8s = self.get_k8s()
        if k8s:
            k8s = self._update_k8s()
        else:
            k8s = self._create_k8s()

        if k8s:
            self.k8s = k8s
            k8s = self._k8s_config()

        return k8s

    def _create_k8s(self):
        required_params = [
            'description',
            'name',
            'service_offering',
            'size',
            'version',
            'zone',
        ]
        self.module.fail_on_missing_params(required_params=required_params)

        docker_registry = self.module.params.get('docker_registry')
        if not docker_registry:
            docker_registry = {
                'url': None,
                'username': None,
                'password': None,
            }

        args = {
            'account': self.get_account(key='id'),
            'controlnodes': self.module.params.get('control_nodes'),
            'description': self.module.params.get('description'),
            'dockerregistrypassword': docker_registry['password'],
            'dockerregistryurl': docker_registry['url'],
            'dockerregistryusername': docker_registry['username'],
            'domainid': self.get_domain(key='id'),
            'externalloadbalanceripaddress': self.module.params.get('load_balancer'),
            'keypair': self.module.params.get('ssh_key'),
            'kubernetesversionid': self.get_version(key='id'),
            'name': self.module.params.get('name'),
            'networkid': self.get_network(key='id'),
            'noderootdisksize': self.module.params.get('root_disk'),
            'projectid': self.get_project(key='id'),
            'serviceofferingid': self.get_service_offering(key='id'),
            'size': self.module.params.get('size'),
            'zoneid': self.get_zone(key='id'),
        }

        self.result['changed'] = True

        k8s = None
        if not self.module.check_mode:
            k8s = self.query_api('createKubernetesCluster', **args)

            poll_async = self.module.params.get('poll_async')
            if poll_async:
                k8s = self.poll_job(k8s, 'kubernetescluster')
        return k8s

    def _update_k8s(self):
        k8s = self.get_k8s()

        args = {
            'id': k8s['id'],
            'kubernetesversionid': self.get_version(key='id'),
            'serviceofferingid': self.get_service_offering(key='id'),
            'size': self.module.params.get('size'),
        }

        if self.has_changed(args, k8s, only_keys=['kubernetesversionid']):
            self.result['changed'] = True

            if not self.module.check_mode:
                upgrade_args = {
                    'id': args['id'],
                    'kubernetesversionid': self.get_version(key='id'),
                }
                k8s = self.query_api('upgradeKubernetesCluster', **upgrade_args)

                poll_async = self.module.params.get('poll_async')
                if poll_async:
                    k8s = self.poll_job(k8s, 'kubernetescluster')

        if self.has_changed(args, k8s, only_keys=['serviceofferingid', 'size']):
            self.result['changed'] = True

            if not self.module.check_mode:
                scale_args = {
                    'id': args['id'],
                    'serviceofferingid': self.get_service_offering(key='id'),
                    'size': args['size'],
                }
                k8s = self.query_api('scaleKubernetesCluster', **scale_args)

                poll_async = self.module.params.get('poll_async')
                if poll_async:
                    k8s = self.poll_job(k8s, 'kubernetescluster')

        return k8s

    def start_k8s(self):
        k8s = self.get_k8s()
        if k8s:
            if k8s['state'].lower() in ['starting', 'running']:
                return k8s

            if k8s['state'].lower() in ['stopped', 'stopping']:
                self.result['changed'] = True

                if not self.module.check_mode:
                    k8s = self.query_api('startKubernetesCluster', id=k8s['id'])

                    poll_async = self.module.params.get('poll_async')
                    if poll_async:
                        k8s = self.poll_job(k8s, 'kubernetescluster')
        return k8s

    def stop_k8s(self):
        k8s = self.get_k8s()
        if k8s:
            if k8s['state'].lower() in ['stopping', 'stopped']:
                return k8s

            if k8s['state'].lower() in ['starting', 'running']:
                self.result['changed'] = True

                if not self.module.check_mode:
                    k8s = self.query_api('stopKubernetesCluster', id=k8s['id'])

                    poll_async = self.module.params.get('poll_async')
                    if poll_async:
                        k8s = self.poll_job(k8s, 'kubernetescluster')
        return k8s

    def absent_k8s(self):
        k8s = self.get_k8s()
        if k8s:
            self.result['changed'] = True

            if not self.module.check_mode:
                k8s = self.query_api('deleteKubernetesCluster', id=k8s['id'])

                poll_async = self.module.params.get('poll_async')
                if poll_async:
                    k8s = self.poll_job(k8s, 'kubernetescluster')

        return k8s

    def _k8s_config(self):
        k8s = self.get_k8s()

        if k8s and 'config' not in k8s:
            config = self.query_api('getKubernetesClusterConfig', id=k8s['id'])
            if config and 'clusterconfig' in config:
                k8s['config'] = config['clusterconfig']['configdata']
                self.k8s = k8s
        return k8s


def main():
    argument_spec = cs_argument_spec()
    argument_spec.update(dict(
        account=dict(),
        control_nodes=dict(type='int'),
        description=dict(),
        docker_registry=dict(
            type='dict',
            options=dict(
                url=dict(),
                username=dict(),
                password=dict(no_log=True),
            ),
            required_together=[('url', 'username', 'password')],
        ),
        domain=dict(),
        load_balancer=dict(),
        name=dict(required=True),
        network=dict(),
        poll_async=dict(type='bool', default=True),
        project=dict(),
        root_disk=dict(type='int'),
        service_offering=dict(),
        size=dict(type='int'),
        ssh_key=dict(),
        state=dict(
            choices=['present', 'enabled', 'disabled', 'absent'],
            default='present',
        ),
        version=dict(),
        zone=dict(required=True),
    ))

    required_together = cs_required_together()
    required_together.extend([
        ('account', 'domain'),
    ])

    required_if = [
        ('state', 'present', ('description', 'service_offering', 'size', 'version')),
    ]

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_together=required_together,
        required_if=required_if,
        supports_check_mode=True
    )

    acs_k8s = AnsibleCloudStackKubernetes(module)

    state = module.params.get('state')
    if state in ['absent']:
        k8s = acs_k8s.absent_k8s()
    else:
        acs_k8s.present_k8s()

        if state in ['disabled']:
            k8s = acs_k8s.stop_k8s()
        else:
            k8s = acs_k8s.start_k8s()

    if k8s and 'state' in k8s and k8s['state'].lower() == 'error':
        module.fail_json(msg="Kubernetes cluster named '%s' in error state." % module.params.get('name'))

    result = acs_k8s.get_result(k8s)
    module.exit_json(**result)


if __name__ == '__main__':
    main()
