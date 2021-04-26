terraform {
  backend "local" {}

  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  // region & credential
  region = "ap-northeast-2"
  access_key = "foo"
  secret_key = "bar"

  // to skip region and credential validation
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
  skip_region_validation      = true
  skip_get_ec2_platforms      = true

  // to avoid S3 bucket validation check error (no such host)
  s3_force_path_style = true

  endpoints {
    // community edition features
    acm              = "http://localhost:4566"
    apigateway       = "http://localhost:4566"
    cloudformation   = "http://localhost:4566"
    cloudwatch       = "http://localhost:4566"
    cloudwatchlogs   = "http://localhost:4566"
    cloudwatchevents = "http://localhost:4566"
    dynamodb         = "http://localhost:4566"
    ec2              = "http://localhost:4566"
    firehose         = "http://localhost:4566"
    iam              = "http://localhost:4566"
    kinesis          = "http://localhost:4566"
    kms              = "http://localhost:4566"
    lambda           = "http://localhost:4566"
    redshift         = "http://localhost:4566"
    route53          = "http://localhost:4566"
    s3               = "http://localhost:4566"
    secretsmanager   = "http://localhost:4566"
    ses              = "http://localhost:4566"
    sns              = "http://localhost:4566"
    sqs              = "http://localhost:4566"
    ssm              = "http://localhost:4566"
    stepfunctions    = "http://localhost:4566"
    sts              = "http://localhost:4566"

    // pro version features
    amplify            = "http://localhost:4566"
    appsync            = "http://localhost:4566"
    athena             = "http://localhost:4566"
    cloudfront         = "http://localhost:4566"
    cloudtrail         = "http://localhost:4566"
    codecommit         = "http://localhost:4566"
    cognitoidentity    = "http://localhost:4566"
    cognitoidp         = "http://localhost:4566"
    ecr                = "http://localhost:4566"
    ecs                = "http://localhost:4566"
    eks                = "http://localhost:4566"
    es                 = "http://localhost:4566"
    elb                = "http://localhost:4566"
    emr                = "http://localhost:4566"
    glacier            = "http://localhost:4566"
    glue               = "http://localhost:4566"
    iot                = "http://localhost:4566"
    kinesisanalytics   = "http://localhost:4566"
    kinesisanalyticsv2 = "http://localhost:4566"
    kafka              = "http://localhost:4566"
    mediastore         = "http://localhost:4566"
    qldb               = "http://localhost:4566"
    rds                = "http://localhost:4566"
    sagemaker          = "http://localhost:4566"
    timestreamwrite    = "http://localhost:4566"
    transfer           = "http://localhost:4566"
    xray               = "http://localhost:4566"
  }
}
