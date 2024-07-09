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
profile = "default"
shared_credentials_files = [ "~/.aws/credentials"] 
}

resource "aws_s3_bucket" "my_s3_bucket" {
  bucket = "terraform_sample_jenkins"
}
 
