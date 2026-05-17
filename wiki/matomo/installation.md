# Installation (Self-hosted & Cloud)

**Summary**: This guide details the installation processes for both Matomo Cloud and Matomo Self-hosted versions.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-03-05

---

## Matomo Cloud Installation
Matomo Cloud is a paid service where Matomo hosts the analytics on their servers.

### Setup Steps
1. **Account Creation**: Sign up for a Matomo Cloud account at [Matomo.org](https://matomo.org/pricing/).
2. **Tracking Code Generation**: Once the account is created, Matomo will provide a unique tracking code for your website.
3. **Implementation**: Copy and paste the tracking code into the `<head>` section of every page you wish to track.

(source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

## Matomo Self-hosted Installation
Matomo Self-hosted is free to use but requires your own server infrastructure and technical setup.

### Prerequisites
- **Web Server**: Apache, Nginx, IIS, etc.
- **PHP**: Version 7.2.5 or greater.
- **MySQL/MariaDB**: Version 5.5 or greater.
- **PHP Extensions**: pdo, pdo_mysql, gd, xml, curl, etc.

(source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

### Step-by-Step Installation
1. **Download Matomo**: Download the latest Matomo package from [Matomo.org/download](https://matomo.org/download/).
2. **Upload to Server**: Extract the zip file and upload the files to your web server using FTP/SFTP or SSH.
3. **Create Database**: Create a new MySQL database and user for Matomo.
4. **Run Installation Wizard**: Open your web browser and navigate to the URL where you uploaded Matomo. Follow the on-screen instructions:
    - **System Check**: Matomo verifies your server meets all requirements.
    - **Database Setup**: Enter your database credentials.
    - **Create Tables**: Matomo creates the necessary database tables.
    - **Super User**: Create the primary administrator account.
    - **Setup Website**: Add the first website you want to track.
    - **Tracking Code**: Copy the generated tracking code.

(source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

### Post-Installation Configuration
- **config.ini.php**: You may need to manually edit this file in the `config/` directory for advanced settings like proxy headers or custom database configurations.
- **Cron Job**: For high-traffic sites, set up a cron job to archive reports automatically rather than processing them on-demand.

(source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

## Troubleshooting
- **Permission Issues**: Ensure the `tmp/` and `config/` directories are writable by the web server user.
- **Missing PHP Extensions**: Check your PHP configuration if the system check fails.

(source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

## Related pages
- [[index|Matomo Analytics Index]]
- [[how-it-works|How Matomo Works]]
