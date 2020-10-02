terraform {
  source = "."
}

include {
  path = find_in_parent_folders()
}

locals {
  group_vars = yamldecode(file("${get_terragrunt_dir()}/${find_in_parent_folders("group.yaml")}"))
}

inputs = {
  cluster_id = local.group_vars["cluster_id"]
  name = "consul"
}
