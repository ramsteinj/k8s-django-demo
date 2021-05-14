terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region = "ap-northeast-2"
  profile = "default"
  //shared_credentials_file = "/Users/a202103023/.aws/credentials"
}
