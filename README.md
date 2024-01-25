# Welcome to Create Nova

Create Nova is your one-stop solution for all your digital marketing and web development needs in Indonesia. We are dedicated to providing top-notch services to small and medium-sized businesses, offering cost-effective solutions to boost your online presence and brand recognition.

Whether you're looking to collaborate with content creators, supercharge your brand's advertising efforts, develop a stunning website, or need bespoke web design services, Create Nova has you covered. Our team of experts is committed to helping you achieve your business goals efficiently and affordably.

In this README, you'll find all the essential information you need to get started with Create Nova, including our services, pricing, and how to get in touch with us. Let's embark on a journey to elevate your brand and expand your digital footprint together!

---

## User Types in Create Nova

Create Nova, hosted on Heroku and utilizing ElephantSQL, offers a diverse range of functionalities catered to different user types. Each user type has access to various features and tools within our platform, ensuring a customized experience that aligns with their specific needs and goals. Here are the four main types of users on Create Nova:

### 1. **Administrators**
As the backbone of Create Nova, administrators have full access to the system. They manage user accounts, oversee site content, ensure the smooth operation of all services, analyze data, generate reports, and maintain the overall health of the platform.

### 2. **Content Creators**
These users are the creative force behind the digital content on our platform. Content creators can design, upload, and manage their digital works. They collaborate with brands, receive feedback, and track the performance of their content.

### 3. **Staff Members**
Staff members are crucial in supporting both the operational and strategic aspects of Create Nova. They assist in managing the platform, provide support to other user types, and help in executing digital marketing and web development projects.

### 4. **Businesses**
Business clients use Create Nova to enhance their online presence and branding efforts. They have access to a range of digital marketing tools, web design services, and can collaborate with content creators. They can manage campaigns, analyze performance, and utilize creative professionals' services.

---

Each user type is integral to the ecosystem of Create Nova, contributing uniquely to the growth and success of digital marketing and web development ventures in Indonesia. Our platform is designed to be intuitive and user-friendly, ensuring a seamless experience for all.

If you're interested in learning more about how Create Nova can help your business, visit our website at [createnova.org](http://createnova.org) or get in touch with our team for personalized assistance.

## Technology Stack

Create Nova is built using a robust and scalable technology stack, ensuring high performance, security, and ease of use. Our choice of technologies reflects our commitment to delivering top-quality services. Here's an overview of the primary technologies used in Create Nova:

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design. It's known for its simplicity and flexibility.
- **Python**: As our core programming language, Python offers readability, efficiency, and a vast ecosystem of libraries and tools.
- **ElephantSQL**: An SQL database service that provides managed PostgreSQL databases. ElephantSQL offers automated backups, data encryption, and scalability.
- **Heroku**: A cloud platform as a service (PaaS) supporting several programming languages. Heroku is used for deploying, managing, and scaling modern apps.

These technologies were chosen for their reliability, ease of integration, and support for agile development practices.

---

## Preliminary Models for User Types

Below are the basic Django models representing the four main types of users in Create Nova. These models are preliminary and may be refined as the development progresses.

### 1. Administrator Model

```python
from django.db import models

class Administrator(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=True)

    def __str__(self):
        return self.username
class ContentCreator(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    portfolio_url = models.URLField(blank=True)

    def __str__(self):
        return self.username
class StaffMember(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.username
class Business(models.Model):
    business_name = models.CharField(max_length=200)
    contact_email = models.EmailField(unique=True)
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.business_name
