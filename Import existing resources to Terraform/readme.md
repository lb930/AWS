# Import existing resources to Terraform

First, create a [configuration file](https://github.com/lb930/AWS/blob/main/Import%20existing%20resources%20to%20Terraform/main.tf) for the source you would like to import in the root module.

Initialise Terraform in your directory and use the ```import``` command to import your resource.

**Syntax**

```terraform import [options] ADDRESS ID```

**Example**

```terraform import aws_s3_bucket_public_access_block.backup-bucket-luisa backup-bucket-luisa```
