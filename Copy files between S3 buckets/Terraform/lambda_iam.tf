resource "aws_iam_role_policy" "lambda_terraform_policy" {
  name = "lambda_terraform_policy"
  role = aws_iam_role.lambda_terraform_role.id

  # Terraform's "jsonencode" function converts a Terraform expression result to valid JSON syntax.
  # Get policy from https://awspolicygen.s3.amazonaws.com/policygen.html
  policy = jsonencode({
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1614892693189",
      "Action": "s3:*",
      "Effect": "Allow",
      "Resource": "*"
    },
    {
      "Sid": "Stmt1614892747838",
      "Action": "logs:*",
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
})
}


resource "aws_iam_role" "lambda_terraform_role" {
  name = "lambda_terraform_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}