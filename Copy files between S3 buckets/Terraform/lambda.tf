locals {
    lambda_zip_location = "outputs/copy_from_s3.zip"
}

data "archive_file" "copy_from_s3" {
  type        = "zip"
  source_file = "copy_from_s3.py"
  output_path = local.lambda_zip_location
}

resource "aws_lambda_permission" "allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.terraform_move_files.arn
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.terraform-luisa.arn
}

resource "aws_lambda_function" "terraform_move_files" {
  filename      = local.lambda_zip_location
  function_name = "terraform_move_files"
  role          = aws_iam_role.lambda_terraform_role.arn
  handler       = "copy_from_s3.lambda_handler"

# Ensures that the Python script is reloaded into AWS if it's updated
  source_code_hash = filebase64sha256(local.lambda_zip_location)

  runtime = "python3.8"

}

resource "aws_s3_bucket_notification" "terraform_luisa_trigger" {
  bucket = aws_s3_bucket.terraform-luisa.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.terraform_move_files.arn
    events              = ["s3:ObjectCreated:*"]

  }

  depends_on = [aws_lambda_permission.allow_bucket]
  
}