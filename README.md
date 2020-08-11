Role Name
=========

Maintain file and directory on a server.

Requirements
------------

None.

Role Variables
--------------

Default variables are set in `defaults/main.yml`.

Dependencies
------------

No dependency on other Ansible Galaxy roles.

Example Playbook
----------------

    - hosts: servers
      vars:
        fd_directories:
          - path: /srv/app01
          - path: /srv/app02
            owner: user01
            group: group01
      roles:
        - { role: hspaans.fd, become: true }

License
-------

MIT

Author Information
------------------

This role was created in 2020 by [Hans Spaans](https://github.com/hspaans).
