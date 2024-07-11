terraform {
  required_version = ">= 1.6.5"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.30"
    }
  }
}
 
provider "aws" {
region  = "eu-north-1"
profile = "sumit"
shared_config_files      = [ "~/.aws/config"] 
shared_credentials_files = [ "~/.aws/credentials"] 
}

resource "aws_s3_bucket" "my_s3_bucket" {
  bucket = "samplejenkinstest"
}
 
