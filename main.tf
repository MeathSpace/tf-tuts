terraform {
  # Required Terraform Version
  required_version = ">= 1.6.5"
  # Required Providers and their Versions
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.30"
    }
  }
}
 
# Settig up AWS Region & Auth
provider "aws" {
#   region  = var.deployment_regions[0]
region  = "eu-north-1"
#   profile = var.aws_profile
profile = "default"
  default_tags {
    tags = {
      "adv/Project"   = "SHIP"
      "adv/Component" = "DataLakeHouse"
      "adv/Stage"     = terraform.workspace
    #   "access-team"   = var.access_team
    #   "cost-center"   = var.cost_center
    }
  }
}
 
