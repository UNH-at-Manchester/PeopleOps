provider "aws" {
  access_key = "AKIAJ2WDHQWIHCCOW25Q"
  secret_key = "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"
  region = "us-east-2"
}
resource "aws_instance" "gp1047-unhm" {
  ami                         = "ami-4191b524"
  instance_type               = "t2.micro"
  ebs_optimized               = false
  monitoring                  = false
  associate_public_ip_address = true

  user_data                   = "${file("setup-env.sh")}"

  availability_zone           = "us-east-2a"
  key_name                    = "gayathri"

  root_block_device {
    volume_type               = "gp2"
    volume_size               = 50
    delete_on_termination     = true
  }
  tags {
    "Environment"= "unhm"
    "Name"= "gp1047-unhm"
  }
}
output "ssh_sandbox" {
  value = "ec2-user@${aws_instance.gp1047-unhm.public_ip}"
}
