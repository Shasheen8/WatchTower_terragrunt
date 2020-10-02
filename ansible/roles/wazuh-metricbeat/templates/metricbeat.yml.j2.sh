output.elasticsearch:
  hosts: ["{{ es_url | default('localhost:9200') }}"]
  username: "elastic"
  password: "<password>"
setup.kibana:
  host: "{{ kibana_url | default('localhost:5601') }}"