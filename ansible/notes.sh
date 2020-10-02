ansible-playbook  hids-elasticsearch-ec2.yml \
--inventory='3.19.7.218,' \
--user=ubuntu \
--become-method=sudo \
--become \
--forks=5 \
--private-key='~/.ssh/icon_node' \
--extra-vars='{"wazuh_manager_version": "3.11.2-1", "beat": "filebeat"}'