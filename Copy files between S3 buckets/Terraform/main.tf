provider "aws" {
  region = "eu-central-1"
}

resource "aws_s3_bucket" "terraform-luisa" {
  bucket = "terraform-luisa"
}

resource "aws_s3_bucket_public_access_block" "terraform-luisa" {
  bucket = aws_s3_bucket.terraform-luisa.id

  block_public_acls = true
  block_public_policy = true
  ignore_public_acls = true
  restrict_public_buckets = true
}

