# Matomo Analytics DB

<aside>
📌 Matomo is an open-source analytics service, which claims to be an alternative to GA3 & GA4.

It is available either as a ‘**self-hosted**’ service (run on your own server, free of Matomo service charges), or run on Matomo-rented servers (paid, also referred to as **‘Cloud’** version)

This guide covers the general functionality, setup, configuration, and maintenance of Matomo for both ‘Cloud’ and ‘self-hosted’ versions.

It doesn’t cover everything related to the developer’s reference guide for Matomo (development, integration, API reference etc.), except for the excerpts that are relevant for Matomo Analytics major setup & functionality, but that can be checked [here](https://developer.matomo.org/).

</aside>

**Table of Contents:**

1. [How Matomo works](https://www.notion.so/Matomo-Analytics-DB-74e2f6cb8f0549379ec3cbe6c6a1a066?pvs=21)

2. [Installation (Self-hosted & Matomo Cloud versions)](https://www.notion.so/Matomo-Analytics-DB-74e2f6cb8f0549379ec3cbe6c6a1a066?pvs=21)

3. [Data collection](https://www.notion.so/Matomo-Analytics-DB-74e2f6cb8f0549379ec3cbe6c6a1a066?pvs=21):

   1. Basic definitions
   2. Pageview data collection specifics
   3. Matomo Tag Manager
   4. Events
   5. Conversions
   6. e-Commerce
   7. [Extras](https://www.notion.so/Matomo-Analytics-DB-74e2f6cb8f0549379ec3cbe6c6a1a066?pvs=21):
      01. Custom Dimensions
      02. UserID
      03. Custom Page title/URL
      04. HeartBeatTimer
      05. Site Search tracking
      06. Campaigns tracking
      07. Additional Attribution Models
      08. Content tracking
      09. Sessions recording
      10. Forms tracking
      11. Video/audio interactions tracking

4. [Managing Matomo](https://www.notion.so/Matomo-Analytics-DB-74e2f6cb8f0549379ec3cbe6c6a1a066?pvs=21):

   1. Roles
   2. Adding a new website
   3. Multiple websites’ tracking (in one Matomo website)
   4. Cross-domain tracking and Roll-ups
   5. How to import data from GA to Matomo

5. [Privacy](https://www.notion.so/Matomo-Analytics-DB-74e2f6cb8f0549379ec3cbe6c6a1a066?pvs=21):

   1. General recommendations
   2. Other procedures to follow
   3. Two forms of consent and respective setup guides
   4. Cookieless tracking
   5. Cookieless tracking based on consent
   6. Data retention

6. [Other features & reports](https://www.notion.so/Matomo-Analytics-DB-74e2f6cb8f0549379ec3cbe6c6a1a066?pvs=21):

   01. AB tests
   02. Heatmaps
   03. Web vitals
   04. Users Flow
   05. Transitions report
   06. Crash Analytics
   07. Real-time report
   08. Visitors log
   09. Visitors Overview
   10. Dashboards
   11. Multi attribution models
   12. Overlay

7. **How Matomo service works (simplified):**

   1. For Matomo Cloud (Matomo’s rented server) version
      1. **Installation:** Installation of the basic tracking code on the website. It looks like this:

         ```jsx
         <!-- Matomo -->

         <script type="text/javascript">

         var _paq = window._paq = window._paq || [];

         _paq.push(['trackPageView']);

         _paq.push(['enableLinkTracking']);

         (function() {

         var u="//{$MATOMO_URL}/";

         _paq.push(['setTrackerUrl', u+'matomo.php']);

         _paq.push(['setSiteId', {$IDSITE}]);

         var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];

         g.type='text/javascript'; g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);

         })();

         </script>

         <!-- End Matomo Code -->
         ```

         <aside>
          ➡️ In your tracking code, **{$MATOMO_URL}** would be replaced by your Matomo **URL** and **{$IDSITE}** would be replaced by the **idsite** of the website you are tracking in Matomo. In similar fashion, by placing tracking codes for event tracking, user interactions other than pageviews can be tracked.

         </aside>

      2. **Data Collection:** Whenever user interacts with the website (pageload occurs for pageview tracking, or in case other tracking codes are inserted, based on respective interaction), basic tracking code/other inserted code is initialised, and a request with the data about the visitor’s pageload/interaction is sent to Matomo’s rented server (cloud).

      3. **Data Processing and Reporting:** Queries are run in the database, populating Matomo UI with visualised data. When user interacts with Matomo UI (goes into reports, refreshes pages, adjusts charts): each chart shows data that is requested by Matomo from the database, where query is run. Then, visualised data is returned from the database and reflected in the Matomo UI

b. For a self-hosted version:

1. **Installation**:
   - A package for self-installation to be deployed to the website’s server (can be obtained from [Matomo.org](http://matomo.org/))
   - Creation of mySQL or similar DB to host data
   - Installation of the basic tracking code on every page of the website.
2. **Configuration**: config.ini file configuration on the website’s server to get website’s data to be hosted in the DB
3. **Data collection**: Whenever user interacts with the website (pageload occurs), data is sent to a self-hosted database running Matomo’s configuration.
4. **Data Processing and Reporting**: Queries are run in the database, populating Matomo UI with visualised data. When user interacts with Matomo UI (goes into reports, refreshes pages, adjusts charts: each chart shows data that is requested by Matomo from the database, where query is run. Then, visualised data is returned from the database and reflected in the Matomo UI

<aside>
⬇️ Further documentation is structured in a way to flesh out the major parts of Matomo’s data collection explanation: is split into the ‘Installation’, ‘Data collection’, and Data Processing and Reporting’ parts respectively.

</aside>

1. **Installation (also applies to new leads)**
   1. For Matomo Cloud (Matomo’s rented server) version
      1. Sign up for a **free 21-day trial** on the [Matomo website](https://matomo.org/start-free-analytics-trial/). Simply provide your email address and website address to begin. If you’d like to add a new lead’s website(s), please consider doing so from a new account, since billing method cane be set on account level only.

         <aside>
          ➡️ By default, the sub-domain of your Matomo instance will be based on your website address. If you prefer a different sub-domain, you can click on **'change'** to enter a different sub-domain of your choice.

         </aside>

      2. After signing up, you will receive an email from Matomo asking you to activate your account. Once you have received the email, you can set your password and gain access to your Matomo account. Make sure to save it in 1password

      3. Once you log in, you'll be presented with your ‘**Start Tracking’** page. On this page, you'll find your unique tracking code ready to be integrated into your website.

      4. Insert a tracking code on each page of the website

         1. Note: if using a GTM method, don’t follow the on-screen instructions. Instead, go your website’s GTM container, create a new tag, and using the Community Template Gallery, import ‘Matomo Analytics (formerly Piwik)’ tag template by ‘trackify-info’. Create this tag in your container, and configure it as a pageview.

- b. For a self-hosted version (see also [Developer’s documentation](https://matomo.org/guide/installation-maintenance/matomo-on-premise-self-hosted/) for more information):

  1. Pre-requisites: to run Matomo, your host needs a couple of things:
     1. **Operating system** such as Linux (Ubuntu, RedHat, CentOS, Raspberry Pi OS, etc.), [Windows](https://matomo.org/faq/matomo-on-windows/), macOS Server or FreeBSD.
     2. **Webserver** such as Apache, [Nginx](https://github.com/matomo-org/matomo-nginx), IIS, LiteSpeed, etc.
        - [Recommended Servers sizing (CPU, RAM, Disks)](https://matomo.org/faq/on-premise/matomo-requirements/)

        - Matomo 4.x requires PHP version 7.2.5 or greater (**the latest PHP 8.x release is recommended**). Older Matomo 3.x required PHP version 5.5.9 or PHP 7.x

        - PHP extensions [pdo](http://php.net/pdo), [pdo_mysql](http://php.net/pdo_mysql) (or the mysqli), [**PHP GD**](https://matomo.org/faq/troubleshooting/faq_34/). The list of PHP extensions you are recommended to install are:

          ```latex
          $ sudo apt-get install php php-curl php-gd php-cli mysql-server php-mysql php-xml php-mbstring
          ```

        - We also recommend the PHP function shell_exec is enabled as it is used for CLI processes. Please see the following FAQ for more information: [How to make the diagnostic “Managing processes via CLI” to display Ok?](https://matomo.org/faq/troubleshooting/how-to-make-the-diagnostic-managing-processes-via-cli-to-display-ok/)
     3. **MySQL** version 5.5 or greater, or MariaDB (recommended)
     4. **Other suggested requirements**:
        - For **medium and high traffic websites**, please see the following FAQ for more information: [Matomo setup for high traffic websites](https://matomo.org/faq/new-to-piwik/faq_137/#faq_137)
  2. Installation:
     1. [→ Click here for detailed instructions on how to create a new database and MySQL user.](https://matomo.org/faq/how-to-install/faq_23484/)

        - When installing Matomo, you will need to specify a MySQL username and password. The MySQL user must have permission to create and alter tables in the database.
        - The MySQL USER should have the permission to SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX, DROP, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, FILE.

     2. Then, to continue with the installation, you need:

        - A web server, shared hosting or dedicated server.
        - Access to your web server (via shell or FTP)
        - A FTP Client (if you are installing Matomo on a remote server)

     3. Download the latest release Matomo 5.0.0 [from here](https://builds.matomo.org/matomo.zip):

        - Unzip the zip file to a folder on your hard drive. This will create a “matomo” folder containing the files and directories.
        - Open your FTP client and upload the Matomo files in ‘binary mode’ to the desired location on your web server. For example using the [Filezilla FTP client](http://filezilla-project.org/), you can enable Binary mode transfer in the top menu Transfer > Transfer type > Binary). All files can be uploaded to a “analytics” sub-directory in your public www folder, for example *http://yourdomain.org/analytics/* or you could setup Matomo in its own subdomain and upload all the files at *http://analytics.example.org/*

        <aside>
         ➡️ If you have SSH access to your server, you can use it instead of FTP as it is much faster: run
         **wget https://builds.matomo.org/matomo.zip && unzip matomo.zip**

        </aside>

     4. Open your web browser and navigate to the URL to which you uploaded Matomo. If everything is uploaded correctly, you should see the Matomo Installation Welcome Screen

        <aside>
         ➡️ If you are not seeing the Welcome screen, also check that your web server such as Apache or Nginx or IIS is configured and working. If there are any problems during the installation, Matomo will identify them and help you out with a solution.

        </aside>

        - Click Next, check if requirements are checked marked and click next again, if not, implement the missing requirements

     5. MySQL Database Setup should be already set and all form fields are filled in, if not, fill it in

        - The super user is the user that you create when you install Matomo. This user has the highest permissions. Choose your username and password: The super user can perform administrative tasks such as adding new websites to monitor, adding users, changing user permissions, and enabling and disabling plugins.
        - Enter the name and URL of the first website you want to track. You can add more websites once the installation is complete
        - Install the JavaScript Tracking Tag generated by Matomo on every page you want to analyze. We recommend placing this code right before the closing </head> tag or in a shared header file included at the top of all your pages.
        - Click *Continue to Matomo »* and log in to your dashboard.

        <aside>
         ➡️ If you want to give other users access to Matomo, or monitor more than one website, or rebrand Matomo or install third party plugins, you will need to use the Administration pages. Click “Administration” in the top menu, then click “Users” to manage users and permissions.

        If your website is a medium or high-traffic website (more than a few hundred visits per day), we highly recommend to [set up auto-archiving cron task](https://matomo.org/docs/setup-auto-archiving/) so that Matomo calculates your reports periodically

        </aside>

1. **Data collection**

   1. **Several basic definitions:**

      1. Visit - a 30min time-out based period of user activity. For unique visitor that comes to the website for the first time - they are a New visitor, if they visit subsequently, based on id - they are Returning visitor
      2. A hit (recorded request in Matomo) can be either a tracked [page view](https://matomo.org/faq/general/what-is-a-hit/), an [event tracking](https://matomo.org/docs/event-tracking/), a [download](https://matomo.org/faq/new-to-piwik/faq_47/), an [outlink](https://matomo.org/faq/new-to-piwik/faq_71/), an [onsite search](https://matomo.org/docs/site-search/) or a [content tracking](https://matomo.org/docs/content-tracking/) request
      3. Unique visitors - amount of unique ids
      4. Entry page - Landing Page, or page that is the first pageview in a visit
      5. Entrances - count of visits that started on a particular page
      6. Exit Page - the last page accessed during a visit
      7. Exit Rate - the ratio of exists on a page to the visits on a page

   2. **When the basic tracking code is installed on every page of the website, this is what is tracked on each page (meaning, with the pageview event)**:

      01. User IP
      02. User Agent: to also detect browser, OS, device type, device used brand and model
      03. Date & time of the request
      04. Page Title
      05. Page URL
      06. Referrer URL
      07. Screen resolution
      08. File downloads
      09. Outbound link clicks
      10. Page speed
      11. Location of the user: country, region, city, longtitude & latitude
      12. Main language
      13. 1st party cookie info: Random unique visitor ID, time of the first visit, time of the previous visit, number of visits

   3. **Matomo Tag Manager**

      1. **General description:**

         - Same basic functionality as GTM:
           - Better management and control over your tags.
           - Code optimization.
           - Less dependency of development team
         - Key differences between MTM and GTM:
           - No live and latest environments, MTM has live, dev, and staging environments instead
           - No workspaces
         - Technical drawbacks:
           - TMS in some ways is like a “black box” containing all the tags on your website, if a visitor blocks the TMS script, it will block all the resources included within it.
             - In comparison to other tag manager solutions, the Matomo TMS is hosted on your website making it unlikely this scenario will happen and with Matomo there are various ways to avoid these problems
         - Privacy concerns:
           - If you are using Matomo Tag Manager only to configure the Matomo Analytics tracking code, then there is no privacy disadvantage over using the Matomo Analytics tracking code directly.
           - If you are using other marketing platforms tags, where data about users is collected and sent, it necessitates consent

      2. **Installation:**

         - When you create a new site in Matomo, the Tag Manager will automatically pre-configure a container with a Matomo tracking code tag for you
         - Activate the Tag Manager either through the top menu “Tag Manager” , or by going to “Administration => Plugins” in the Matomo property UI
         - Find the tracking code within the ‘Install code’ menu in MTM
           - If you want to create a container for an already existing site, or create an additional container, log in to your Matomo now and click on “Tag Manager => Manage Containers”.
         - Now that you have created the container, it is time to embed the container into your website. To do this, you can click on the “Install Code” icon on the left menu. You will see three options (dev, stage, live).
         - A simple installation will only need a Live environment. However, if you are working on websites where security and stability are critical, you will likely need to add a Dev and Staging environment.
         - Picking up any of those three options will end up in a slightly different container tracking code. Whatever the option you choose, all you need to do is to copy / paste this snippet of code as high as possible on your website. In most cases you will want to copy the code for the “Live” environment.
           - MTM dashboard in Matomo UI lets you easily switch between the containers

         <aside>
          ➡️ If you want to keep using GTM, but don’t want MTM to use the dataLayer values that it sets, simply check the box in the ‘Edit container’ screen.

         This can be found by going to Tag Manager > Manage Containers and clicking the ‘Edit Container’ icon next to the container you wish to update.

         </aside>

      3. **Usage**

         - **Tags in MTM:**

           - The tag configuration consists of three main parts:
             - A section where you configure the tag type itself (Matomo Analytics, Google Analytics, Facebook conversion pixel, Remarketing tag etc.), and what it should do or how the tag should behave, for example you may configure a Matomo Tracking URL or your Google Analytics Property ID. The available form fields in this section differ from tag to tag.
             - A section where you configure when this tag should be executed (or blocked). This is done by assigning a so called trigger. Only when such a trigger is being triggered, the tag will be executed.
             - Advanced settings that let you configure the setup more, for example how often the tag should be executed, limit the date range when the tag should be executed, and more

         - **dataLayer:**

           - Matomo supports GTM’s dataLayer, but if you’d like to use a new one, you will need to add the following lines of code before your container tag:

             ```jsx
             <script>

             var _mtm = _mtm || [];

             </script>

             // As this dataLayer object is empty, 
             // you will need to insert an extra line of code
             // in order to push variables into it, so it will
             // look something like this if you’re hardcoding it:

             <script>

             var _mtm = _mtm || [];

             _mtm.push({'weather': 'sunny'});

             </script>
             ```

         - **Multiple environments testing:**

           - To set this up with Matomo Tag Manager, you can follow these steps:
             - [Create each “Website” you wish to track as its own measurable in Matomo](https://matomo.org/faq/how-to/create-and-manage-websites/) (For example a “Measurable/Website” for each Staging, Dev or Production site)
             - Create a “Lookup Table” as explained in Manage Variables in Matomo Tag Manager (see the section [Advanced Variable Settings Default Value Lookup Table](https://matomo.org/faq/tag-manager/manage-variables-in-matomo-tag-manager/#advanced-variables-settings-default-value-lookup-table)), setting each hostname/URL to the URL of your different environments. Be sure to set the value of each URL to the correct Site ID for each environment
             - Change the Site ID configured in your “Matomo Configuration” variable to the new Lookup Table variable that was just created, for example {{SiteID}}
             - Deploy the different “Environments” you wish to track to each applicable website. For example the “Staging” environment tracking code should be deployed to your “Staging” website and the “Dev” environment to your development website.

         - **Debug mode in MTM:**

           - The use of the preview / debug mode is straightforward; once your tags, triggers and potential variables are set, just click on ‘Preview / Debug’ in the MTM interface

           - You will then be notified straight away through the dashboard that you are in the selected mode:

             - Enter the **URL** you want to debug and press ‘debug’ to start debug mode for that site.

             <aside>
               ➡️ In some cases you will need to append
               **?mtmPreviewMode=YourContainerID&mtmSetDebugFlag=1** to the URL of your website to see the debug console

             </aside>

         - **Versions and publishing:**

           - Versions let you save a copy of the current configuration of a container so you can go back to a previous version of a container if you need to do so.
           - You have the choice to not publish it yet, which will give an opportunity for other users to see the modifications you performed and to provide their feedback. It also makes it easy to recover from mistakes, and lets you easily find all previously deployed tags, triggers, and variables. Once you are happy with your current configuration, you can publish it to a specific environment (Dev, Staging, Live)
           - To publish:
             - In the left menu, click “Publish”.
             - Add a version name, for example ‘Analytics v3’.
             - Click the green “Create New Version And Publish Release” button.

         - **Migrating from GTM to MTM:**

           - Migrating from GTM to MTM is currently a manual process because there are enough differences and quite a bit of complexity. You probably want to start by creating your container in MTM and making sure you have all of the environments you’re used to using. Once that’s done, you can proceed with the following:
             - Look through your list of GTM variables and try to create similar ones in MTM. A good place to start becoming more familiar with MTM variables is the [Variables user guide](https://matomo.org/guide/tag-manager/variables/).
             - Then, look through all of your GTM triggers and try to duplicate them in MTM. You can find details about MTM triggers in the [Triggers user guide](https://matomo.org/guide/tag-manager/triggers/).
             - Once your variables and triggers are in place, you can try to duplicate all of your GTM tags in MTM. Read up on MTM tags in the [Tags user guide](https://matomo.org/guide/tag-manager/tags/).
             - Copy the MTM install code and insert it near or in place of the GTM snippet in your website’s HTML header. For more information, you can look through the [Install a tag manager container FAQ](https://matomo.org/faq/tag-manager/install-a-tag-manager-container-on-your-site/).
             - You should then be ready to preview and debug your tags. You can read about that in the [Preview/debug FAQ](https://matomo.org/faq/tag-manager/preview-debug-a-tag-manager-container/).
             - If everything looks good, you can create a new version and publish it. That process is described in the [Versions and publish user guide](https://matomo.org/guide/tag-manager/versions-and-publish/).

   <aside>
    ⬇️ Other things that can also be tracked to Matomo, aside from the pageviews:

   </aside>

   **d. To track any user interaction with Matomo (events)**, there are two main ways. The first is by adding snippets of JavaScript code to your website itself. The second is with the Tag Manager plugin built into Matomo:

   1. You can manually call the JavaScript function trackEvent() based on the user interaction you’d like to track. Custom events consist of four primary components which need to be configured, only two of which are required:

      - **Category (Required)** – This describes the type of events you want to track. For example, Link Clicks, Videos, Outbound Links, and Form Events.
      - **Action (Required)** – This is the specific action that is taken. For example, with the Video category, you might have a Play, Pause and Complete action.
      - **Name (Optional – Recommended)** – This is usually the title of the element that is being interacted with, to aid with analysis. For example, it could be the name of a Video that was played or the specific form that is being submitted.
      - **Value (Optional)** – This is a numeric value and is often added dynamically. It could be the cost of a product that is added to a cart, or the completion percentage of a video.

      <aside>
       ⬇️ For example, if you wanted to track a click on a JavaScript menu, you could write:

      </aside>

      ```html
      <a href="#" onclick="_paq.push(['trackEvent', 'Menu', 'Freedom']);">Freedom page</a>
      ```

   2. Using Matomo Tag Manager (much like the Google’s version). Example with email link clicks tracking:

      - Set up and configure Matomo Tag Manager (create a website, a container, and install the container code on the website)
      - Click on **Tag Manager** in Matomo and visit the **Tags** page.
      - Click the big green button to **Create New Tag**.
        - Select the **Matomo Analytics** tag type.
        - Give your [***Tag***](https://matomo.org/docs/tag-manager/#tags) a descriptive name. For example; **Matomo Event – Email Link Click**
        - Confirm your Matomo configuration. If you are not sure, use the default configuration.
        - Select **Event** as the **Tracking Type**.
        - You are now ready to add your event structure in the next few fields. Following our example, this would be:
          - **Event Category:** Contact
          - **Event Action:** Email Link Click
          - **Event Name:** {{ClickDestinationUrl}}
      - Create a trigger using All links click option, then specify ->
        - Select **Click Destination URL** in the first field
        - Select **starts with** for the second field.
        - Type ***mailto:*** in the last field which is the prefix used to create email links.
        - Finalise the trigger by clicking the big green button to **Create New Trigger**.
      - Now that the Trigger is attached to the Tag settings you can click to **Create New Tag**.
      - Publish changes

   <aside>
    ➡️ You can find the Events report under the ‘**Behaviour’** section in Matomo.

   </aside>

   **e. To trigger a goal conversion (conversions):**

   1. Visit the ‘**Goals’** section in Matomo and then click over to ‘**Manage Goals’**.

      - This page will show any existing goals you have along with a large green button to ‘**Add A New Goal’**. Clicking this button will bring up the ‘**Update Goal’** view where you can add all of the required details.
      - Additionally can track multiple goals per visit (toggle), or set up conversion funnels as in GA3.

   2. Create the goal in that menu, then either continue to set the trigger conditions within the same menu, or push an event with the same index you set when configuring the goal in Matomo from your website:

      ```jsx
      // logs a conversion for goal 1

      _paq.push(['trackGoal', 1]);

      // You can also register a conversion for this goal
      // with a custom revenue. For example, you can generate
      // the call to trackGoal() dynamically to set the revenue
      // of the transaction:

      // logs a conversion for goal 1 with the custom revenue set

      _paq.push(['trackGoal', 1, <?php echo $cart->getCartValue(); ?>]);
      ```

   <aside>
    ➡️ In the **Goals** report you have:

   - A time-series graph with conversion count + eCR;
     - You have options to modify/engage with the graph (change period, export data, view/add annotations).
   - Below that, you will find summary cards for all conversions per given period of time (conversion count + eCR + revenue);
   - Below that, you will see data in the same way as in the previous point, but broken down by each goal;
     - If you would like to review any of the goals in more detail, simply click on the goal title, and it will take you to a dedicated page for that goal with more detailed graphs and data.
   - Then we also have goals breakdown reports by:
     - Referrers (channel, search engine, keyword, website, campaign);
     - Engagement (location, country, continent, region, city, device type, model & brand).

   </aside>

   **f. eCommerce tracking has a two-phase setup process:**

   1. Enable Ecommerce tracking within the Matomo interface:

      - For a new website:
        - Log into Matomo as a [Super User](https://matomo.org/faq/general/faq_35/).
        - Click **All Websites** in the blue top menu to bring up the list of your existing sites (if any) and then click to **Add a new website**. This will bring up some options to define what you are measuring.
        - Click on the **Website** button to confirm.
        - Complete the necessary details about the website, such as the name and URL. You will find a short description of what each field should contain in a grey box next to it.
        - Several fields down you will reach the **Ecommerce** settings.
        - Set the currency in the field below. Click Save
      - For the existing website:
        - Click on the cog icon in the **Top Menu** to load the **Settings** page
        - Visit the **Measurables/Websites** section from the **Main Navigation** on the left-hand side.
        - Find the website you’d like to update and click the **Edit** icon
        - Scroll down the page until you reach the **Ecommerce** dropdown menu, and select ***Ecommerce enabled***.
        - Select the appropriate **Currency** option in the dropdown that follows.
        - Click Save.

   2. Enable Ecommerce Tracking on Your Ecommerce Platform.

   <aside>
    ➡️ In this example are M2 module specifics, solutions for other CMS can be found [here](https://matomo.org/integrate/#ecommerce-online-shops)

   </aside>

   - Purchase a [module](https://commercemarketplace.adobe.com/jajuma-module-matomoanalytics.html)
   - Install it on the website as outlined in the module’s documentation
   - Configure (pageviews, eCommerce events, Matomo Tag Manager script, Matomo to M2 dashboard and other features):
     - Go to the M2 backend -> Jajuma -> Matomo analytics -> Configuration

       - Check the ‘General’ tab and configure endpoint (URL + SiteID), other fields are optional
       - Check the ‘Dashboard’ tab and fill all the fields there: (date range (automatic) + access token)

       <aside>
         ➡️ Dashboard is accessible in Dashboard -> Matomo -> Matomo Dashboard

       </aside>

       - Check the ‘Privacy configs’ tab and choose if website should respect user’s right to not be tracked if they wouldn’t like to
       - Check the ‘JS tracking configs’ (pageviews, cross-subdomain tracking, heartbeat configuration, proxy for avoiding ad blockers, tracker name)

       <aside>
         ➡️ For tracker name changes in production mode, please run **bin/magento s:d: and clear cache**

       </aside>

       - Check the ‘eCommerce’ tab, enable either JS or PHP (server-side) tracker.

       <aside>
         ➡️ For server-side, make sure to configure tracker access token above in ‘General’ section.

       Here you should also choose if to push all orders or only completed (paid for) ones, and if there should be delay in pushes for events

       </aside>

       - Check the ‘Matomo Tag Manager’ tab, enable it, enter container id to your Matomo website. Then:
         - Copy the JSON file
         - Go to your container in Matomo
         - Select “Versions” tab and Click “Import” button
         - Paste the JSON formatted data that you exported previously
         - Replace “SITE_ID” in JSON with your Matomo SiteID
         - Click ”Overwrite current draft with this version” button

   **iii. You can alternatively (instead of using the module) use the JS-based triggers to send eCommerce data to Matomo. You still need to enable Ecommerce setting in the Matomo Admin Panel for this to work**

   - PLP view

   ```jsx
   // Push Category View Data to Matomo - Fill category dynamically

   _paq.push(['setEcommerceView',

   false, // Product name is not applicable for a category view.

   false, // Product SKU is not applicable for a category view.

   "Books", // (Optional) Product category, or array of up to 5 categories

   ]);

   // You must also call trackPageView when tracking a category view

   _paq.push(['trackPageView']);
   ```

   - PDP view

   ```jsx
   // Push Product View Data to Matomo - Populate parameters dynamically

   _paq.push(['setEcommerceView',

   "0123456789", // (Required) productSKU

   "Ecommerce Analytics Book", // (Optional) productName

   "Books", // (Optional) categoryName

   9.99 // (Optional) price

   ]);

   // You must also call trackPageView when tracking a product view

   _paq.push(['trackPageView']);
   ```

   - Add/remove to cart as a cart update.

   <aside>
    ➡️ To track cart additions and removals, your cart system will need to send the details for every item that remains in the cart after a user adds or removes an item, including those already submitted from prior **Add to Cart** clicks

   </aside>

   ```jsx
   // An addEcommerceItem push should be generated for each cart item,
   // even the products not updated by the current "Add to cart" click.

   _paq.push(['addEcommerceItem',

   "0123456789", // (Required) productSKU

   "Ecommerce Analytics Book", // (Optional) productName

   ["Books", "Best sellers"], // (Optional) productCategory

   9.99, // (Recommended) price

   1 // (Optional, defaults to 1) quantity

   ]);

   // Pass the Cart's Total Value as a numeric parameter

   _paq.push(['trackEcommerceCartUpdate', 15.5]);
   ```

   - Purchase

   <aside>
    ➡️ Typically tracked on the order confirmation page after payment has been confirmed.

   </aside>

   ```jsx
   // Product Array

   _paq.push(['addEcommerceItem',

   "01234567890", // (required) SKU: Product unique identifier

   "Ecommerce Analytics Book", // (optional) Product name

   "Books", // (optional) Product category. You can also specify an array of up to 5 categories eg. ["Books", "New releases", "Biography"]

   9.99, // (Recommended) Product Price

   1 // (Optional - Defaults to 1)

   ]);
   ```

   The second part of the order update code passed to Matomo is a summary of the order. At a minimum, it should include an order ID and the total revenue value. The variables passed, in order, are:

   - **orderId** (Required) – String – A unique reference number to avoid duplication.
   - **grandTotal** (Required) – Integer/Float – The order total revenue including tax & shipping with any discounts subtracted.
   - **subTotal** (Optional) – Integer/Float – The order total excluding shipping.
   - **tax** (Optional) – Integer/Float -The amount of tax charged.
   - **shipping** (Optional) – Integer/Float – The amount charged for shipping.
   - **discount** (Optional) – Integer/Float/Boolean – Discount offered? Default to false. Otherwise, you should include a numeric value.

   ```jsx
   // Order Array - Parameters should be generated dynamically

   _paq.push(['trackEcommerceOrder',

   "000123", // (Required) orderId

   10.99, // (Required) grandTotal (revenue)

   9.99, // (Optional) subTotal

   1.5, // (optional) tax

   1, // (optional) shipping

   false // (optional) discount

   ]);
   ```

<aside>
➡️ eCommerce reports:

1. Metrics and parameters that can be seen in eCommerce reports:
   01. **Ecommerce orders**
   02. **Products Purchased**
   03. **Total Revenue**
   04. **Subtotals** – The order subtotal, excluding shipping and tax.
   05. **Tax**
   06. **Shipping**
   07. **Discounts**
   08. **Average Order Value (AOV)**
   09. **Ecommerce Orders Conversion Rate**
   10. **Abandoned Carts** – The total number and potential revenue of visits where people added products to their shopping cart but ultimately left the site without making a purchase.
   11. **Revenue per visit**

\*\*\*\*2. Reports:

1. **Ecommerce Overview** page, Chart 1:
   1. Time series chart with purchases per day (can also display data increments by the: **Day**, **Week**, **Month** or **Year**.). Optionally can select metrics shown in the chart instead:
      - Ecommerce Orders
      - Conversion Rate
      - Total Revenue
      - Purchased Products
      - Average Order Value

Note: Can also export or annotate the data

b. **Ecommerce Overview** page, Chart 2:

1. The following statistics are displayed within the sparkline summary card:
   - Ecommerce Orders
   - Total Revenue
   - Average Order Value
   - Ecommerce Orders conversion rate
   - Purchased Products
   - Visits with Abandoned Cart
   - Revenue left in cart

Note: If you would like a closer look at any of these statistics over time, you can click on the summary to update the full-sized evolution graph above this section with the relevant data

1. Other reports:

   **c. Cart Abandonments overview**

   **d. Orders overview** (revenue, subtotals, tax, shipping, discounts, per each order)

   **e. E-commerce Log** (granular session-level data)

   **f. Sales and conversion rates in a table by either:** Name, SKU, or Category

   **g. Sales by referrers/channels/search engines/keywords**

   **h. Sales engagement** (days & visits to conversion)

   **i.User location** (country, continent, region)

   **j. Devices** (type, model, brand)

   **k. Custom dimensions**

</aside>

```
  **g. Extras that can also be tracked in Matomo:**
```

1. **Custom dimensions:**

Custom dimensions are extra event parameters that can be supplied with the event sent from the website to the Matomo server. There are two types of custom dimensions:

- Visitor type (typically have consistent value per session. Can be seen in the Matomo ‘Visitor’ reports, or in the ‘User IDs’ page in the ‘Visitor’ reports, if it’s UserId that is set up)
- Action type (usually dynamically changed based on user interaction more than once per session. Can be seen in the Matomo ‘Behaviour’ report).

<aside>
➡️ You can have 5-15 custom dimensions per type, and they can only be deactivated, not deleted.

</aside>

To track custom dimensions, Install the plugin [Matomo Marketplace (CustomDimensions plugin)](https://plugins.matomo.org/CustomDimensions). You then have two options:

- Set up trigger as every Page URL / Page Title + Value for the custom dimension using Regex rules in the admin section (Administration -> Custom dimensions) for either action or visit type of custom dimension;

- Activate a custom dimension in said admin panel section + push a value from the website. Again, this works for either visit or action type:

  ```jsx
  _paq.push(['setCustomDimension', customDimensionId = 1, customDimensionValue = 'Member']);

  _paq.push(['trackPageView']);

  // it’s imperative to push pageview after 
  // custom definitions are set on the page
  ```

  <aside>
    ➡️ Please note once a Custom Dimension is set, the value will be used for all following tracking requests and may lead to inaccurate results if this is not wanted. To delete a Custom Dimension value after a tracking request call:

  </aside>

  ```jsx
  _paq.push(['deleteCustomDimension', customDimensionId]);
  ```

  <aside>
    ➡️ It is possible to set a Custom Dimension for one specific action only, so you don’t have to delete it after it’s been pushed with the action you need it for. The advantage is that the set dimension value will be only used for this particular action and you do not have to delete the value after a tracking request:

  </aside>

  ```jsx
  _paq.push(['trackEvent', category, action, name, value, {dimension1: 'DimensionValue'}]);

  _paq.push(['trackSiteSearch', keyword, category, resultsCount, {dimension1: 'DimensionValue'}]);

  _paq.push(['trackLink', url, linkType, {dimension1: 'DimensionValue'}]);

  _paq.push(['trackGoal', idGoal, customRevenue, {dimension1: 'DimensionValue'}]);
  ```

  <aside>
    ➡️ You may also set multiple dimension values like this:

  </aside>

  ```jsx
  _paq.push(['trackPageView', pageTitle, {dimension1: 'DimensionValue', dimension4: 'Test', dimension7: 'Value'}]);
  ```

**ii. For UserID:**

[User ID](https://matomo.org/docs/user-id/) is a feature in Matomo that lets you connect together a given user's data collected from multiple devices and multiple browsers. There are three steps for implementing User ID:

- You must assign a unique and persistent non-empty string that represents each logged-in user. Typically, this ID will be an email address or a username provided by your authentication system.

- You must set the user ID for each pageload and pageview, otherwise the pageview will be tracked without the user ID set.

- You must then pass this User ID string to Matomo via the **setUserId** method call just before calling any of the track functions (trackPageview, trackEvent, trackGoal, trackSiteSearch, etc.) for example:

  ```jsx
  _paq.push(['setUserId', 'USER_ID_HERE']);

  _paq.push(['trackPageView']);

  When the user has logged out and a User ID is not available anymore, it is recommended to notify Matomo by calling the resetUserId method before trackPageView.

  // User has just logged out, we reset the User ID

  _paq.push(['resetUserId']);

  // we also force a new visit to be created for the pageviews after logout

  _paq.push(['appendToTrackingUrl', 'new_visit=1']);

  _paq.push(['trackPageView']);

  // we finally make sure to not again create a new visit afterwards
  // (this is important for Single Page Applications)

  _paq.push(['appendToTrackingUrl', '']);
  ```

Alternatively, you can do the same with Matomo Tag Manager:

The method for configuring User ID tracking with Matomo Tag Manager will vary depending on how your website has been built, but the general idea is as follows.

- Install and configure Matomo Tag Manager for your site.
- Create a variable called ***UserID*** that captures each visitor’s unique user identifier, assuming that the first 2 steps outlined at the [beginning](https://www.notion.so/49959b43859948bab60766f031a2d0fd?pvs=21) are fulfilled.
- Create or update your ***Matomo Configuration* variable** to collect the ***UserID***. Assuming you named your User ID variable in the last step ***UserID***, you would scroll down to the User ID text field and input ***{{UserID}}*** to pull the values captured by that variable into your Matomo tracking configuration.
- Preview and publish your updated Matomo container.

<aside>
➡️ Where to see UserID data in Matomo UI:

- You can access the **User IDs** report within the **Visitors** section of the main navigation menu within Matomo. This report will show you a table of all registered User IDs that have interacted with your site during the selected reporting period.
  - The User IDs table can also be updated to include more engagement metrics. To do this, hover your mouse over the table so the icons menu appears in the bottom left. Then click on the ***table icon*** to reveal the alternative visualisation options. Then click on **Display a table with Visitor engagement metrics**
  - The above statistics are useful for analysing your groups of users, but it is also possible to get even more granular data for a single user. If you hover your mouse over any of the User ID rows, you will see three green icons appear. Clicking on any of these will allow you to dig even deeper into visits by that user (Visitor profile)

</aside>

**iii. Custom Page title/URL:**

- By default Matomo uses the title of the HTML page to track the page title, you can customise it by using the function **setDocumentTitle**:

  ```jsx
  _paq.push(['setDocumentTitle', document.title]);

  _paq.push(['trackPageView']);
  ```

- Similarly, for setting a different URL, use the function **setCustomURL**:

  ```jsx
  _paq.push(['setCustomUrl', 'https://yourdomain.com/your-new-page-url']);

  _paq.push(['trackPageView']);
  ```

- If you track **multiple sub-domains in the same website**, you may want your page titles to be prefixed by the sub-domain make it easy for you to see the traffic and data for each sub-domain. You can do so in the following way:

  ```jsx
  _paq.push(['setDocumentTitle', document.domain + "/" + document.title]);

  _paq.push(['trackPageView']);
  ```

**iv. It is possible to configure Matomo so that it accurately measures the time spent in the visit.** To better measure time spent in the visit, add to your JavaScript code the following:

```jsx
_paq.push(['enableHeartBeatTimer']);
```

The heart beat request is executed when:

- switching to another browser tab after the current tab was active for at least 15 seconds (can be configured see below).
- navigating to another page within the same tab.
- closing the tab.

**v. Site Search**

Matomo can automatically read URL parameters that will contain the search keyword. Thus, to use SiteSearch tracking:

- Go to Matomo’s **Administration > Websites > Manage** (or **Administration > Measurables > Manage**).
- Edit your chosen website via the pencil icon located on the right, and you can then enable or disable **Site Search tracking** for your website.

However, you can also record the site search keywords manually using the JavaScript function **trackSiteSearch(keyword, category, searchCount)**

```jsx
_paq.push(['trackSiteSearch',

// Search keyword searched for

"Banana",

// Search category selected in your search engine.
// If you do not need this, set to false

"Organic Food",

// Number of results on the Search results page.
// Zero indicates a 'No Result Search Keyword'.
// Set to false if you don't know

0

]);

// We recommend **not to call** trackPageView() on the Site Search Result page

// _paq.push(['trackPageView']);
```

<aside>
➡️ The 'keyword' parameter is required, but ‘category’ and ‘searchCount’ are optional.

</aside>

<aside>
➡️ On your website, on standard pages, you would typically have a call to record Page views via *matomoTracker.trackPageView()*.

On your search result page, you would call **instead** only *piwikTracker.trackSiteSearch(keyword, category, searchCount)* function to record the internal search request.

</aside>

<aside>
➡️ All Site Search reports:

- Under **Visitors > Overview**, the total number of Site Searches is reported alongside the total number of Pageviews, Downloads, Outlinks, Events, and which Keywords were used.
- Under **Behaviour > Site Search**, you will find all the detailed reports, such as the Top Internal Searches
- You will also find the **Pages Following a Site Search** report, which displays the pages which are most searched for and clicked on in your search engine.

</aside>

**vi. Campaigns tracking:**

Default parameters:

- mtm_campaign
- mtm_keyword

Custom parameters (require Marketing Campaigns Reporting plugin):

- mtm_source - source where user came from
- mtm_medium - medium where user came from
- mtm_content - specific information about link or type of content user clicked
- mtm_cid - a unique identifier for your specific ad
- mtm_group - the audience type of the campaign user clicked
- mtm_placement - placement on an advertising network e.g. newsfeed, sidebar, home-banner, etc.

<aside>
➡️ Plugin also automatically detects the utm parameters: **utm_campaign, utm_source, utm_medium, utm_term, utm_content, utm_id**

</aside>

<aside>
➡️ Here’s also Matomo’s own [**URL builder**](https://matomo.org/docs/tracking-campaigns-url-builder/)

</aside>

**vii. ‘Last non-Direct’ is the default attribution model. Multi-channel attribution** extension, which is purchased separately, opens up other attribution models:

- **Last Interaction** – This is the most commonly used attribution model on the web. It simply tracks how people reached you in the session where they made a purchase.
- **Last Non-direct** – This is based on the same model above, but as a direct visit is often from a bookmark or non-advertising related source, it might be more useful to review the last meaningful source that you can use for optimising your future marketing.
- **First Interaction** – This allows you to see how somebody first found your website, even if they subsequently made several visits to your site from different traffic sources.
- **Linear** – In this model, the credit for a sale is split evenly between all interactions no matter at what stage of the conversion process they occurred.
- **Position Based** – This allows you to allocate most of the credit (40% each) to both the first and last interaction as these are often the most important and then split the remaining 20% across all channels that assisted with the sale in between.
- **Time Decay** – The final attribution model is based on how long an interaction occurred before a sale. It still assumes that the last interaction is the most relevant for pushing a visitor into a sale, however, it also allocates a decreasing amount of credit to the traffic source of each preceding visit to the website

**viii. Content tracking:**

Matomo can track content (banners, ads, etc.) on your website, specifically when it was viewed or clicked on.

- Add the **data-track-content** attribute to the HTML of an element you’d like to track. You can also use [more attributes](https://matomo.org/faq/how-to/how-do-i-markup-content-for-content-tracking/) when working with those elements.
  - If you only want to track an impression when the content is visible on screen, then you need to add a listener to the element you marked up with attributes in the previous step, and to push the following code at the right time:

    ```jsx
    _paq.push(['trackPageView']);

    _paq.push(['trackVisibleContentImpressions']);
    ```

    > There is little to no documentation about content clicks tracking, but that may be updated / reviewed shall the need arise

**ix. Sessions recordings**

- In the administration menu, click on “Session Recordings”, and then “Manage Session Recordings”.
- To record new sessions, click on “Create new session recording” in the bottom left. To edit a session recording, simply click on the “edit” icon next to the name of a previously created recording.
- When you create or edit a session recording, all you need to do is defining a name for the recording. That’s it.
  - Optionally, you can choose to record activities only on a specific target page or target pages. To do this, you can choose between “URL”, “URL path”, “URL parameter” attributes and comparisons like “equals”, “starts with”, “contains”, “matches the regular expression”, and many more.
  - Additionally, you can:
    - Define if Sessions should be recorded only for active users (if they scroll, click)
    - Define if Sessions should be recorded only if users have spent at least a certain time on your web page (Min. Session Time)
    - Disable the recording of keystrokes that user enter into text form fields (Capture keystrokes)
    - Define how many sessions should be recorded (Number of sessions)
    - Define how likely a user’s session should be recorded (Sample Rate)

<aside>
➡️ Session recording reports:

Go to Matomo. In the left menu click “Session Recordings” and then select a session recording of your choice.

- A session recording report shows you a list of all recorded page views, including useful information like the time of the session initialization, the duration of the session, the viewport resolution, the location, device information, and more.
- To replay a recorded session, to delete a recording, or to view the [visitor profile](https://matomo.org/docs/user-profile/), hover a row and select a row action.

</aside>

**x. Forms tracking (paid feature):**

If a relevant extension is purchased, Matomo will automatically discover your online forms and capture users’ interactions with them. However, if you’d like to configure the forms manually:

- Click in the administration menu on “Forms”, and get to the “Manage Forms” screen.
- To create a form, click on “Create new form” in the bottom left. To edit a form, simply click on the “edit” icon next to the name of a previously created form. In both cases, you will end up in a menu where you can finalize form tracking by setting the following:
  - Matching forms conditions: It lets you specify which of your online forms should be tracked into this form. You can do this by defining criteria based on form names and form IDs. If you want to, you can track many different forms into one form in Matomo. You can also leave these fields empty and track a form only by its page URL or URL path;
  - Restrictions of the form tracking to certain pages;
  - When a form should be considered as completed successfully: either submission = conversion, or some other interaction is a conversion.

<aside>
➡️ Forms tracking reports:

1. The “Overview” report gives you an overview over all your form metrics and how they evolve over time.
2. Matomo adds one menu item for each of your forms. Select any form to get all the detailed reports about this form:
   - The form summary shows you information about the chosen form, the possibility to view the visitor log with all the visitors that have started, submitted or converted this form, and a table letting you see all the fields within that form;
   - Below the summary you see an evolution graph and lots of sparklines showing you at a glance how important form metrics like the “Form conversion rate”, “Number of form viewers”, “Number of starters” and others perform over time;
   - A Page URL report showing you all the important form metrics for each page where this form is embedded. This lets you see whether your users interact differently with the same form on different pages.
3. Form Analytics adds seven other reports to learn everything about how your users interact with your form fields:
   - The drop-off report is critical to find out where you lose your visitors on a form. It shows which field a visitor focused on or interacted with last before abandoning the form;
   - The entry fields report shows you with which fields your users interact with first when they start filling out a form;
   - Which fields your visitors spend a lot of time on, and where they hesitate the most;
   - Field size: Do your visitors need to type a lot? This may reduce conversion rates as it results in too much effort for your visitors;
   - Find out which fields are used the most or the least;
   - Most corrected fields: Discover where your visitors have the most problems filling out your form;
   - Fields that are often left blank. These can likely be removed which in turn will improve your conversions.

</aside>

**xi. Video / audio interactions tracking**

If you have already embedded the [Matomo JavaScript Tracking Code](https://developer.matomo.org/guides/tracking-javascript-guide) into your website, the Media Analytics will automatically start tracking the usage of video and audio on the website.

<aside>
➡️ Since the video & audio player tracking code is directly added in your Matomo JavaScript tracker file / matomo.js, as long as the file matomo.js in your Matomo directory is writable by the webserver / PHP, audio and video should be automatically tracked. 

To check whether this works by default for you, login into Matomo as a Super User, go to Administration, and open the "System Check" report. If the System Check displays a warning for "Writable Matomo.js" then [learn here how to solve this](https://developer.matomo.org/guides/media-analytics/setup#when-the-matomojs-in-your-piwik-directory-file-is-not-writable). Otherwise, no need for additional changes.

</aside>

<aside>
➡️ Video / Audio tracking reports:

Go to Matomo. In the left menu click “Media” and then select a Media report of your choice.

- The “Overview” report gives you an overview over the media metrics and how they evolved over time;
- With the Real-time report you always have an eye on what is happening right now;
- The Video & Audio reports show you critical metrics into how and when your media was consumed;
- The Audience Log & Audience Map lets you know where your audience is located, who they are, and what they did before and after watching a video or listening to audio.

</aside>

1. **Managing Matomo**

   1. **Roles**

      1. The **View** role allows a user to see reports for a website.
      2. The **Write** role is the same as the **View** role, except the user can also create (and update and delete) a website’s Goals, Forms, Funnels, A/B tests, Heatmaps, Session Recordings, etc.
      3. The **Admin** role is one step above the **Write** role in that it allows a user to both see reports, configure those reports and the website itself, and also manage user access for the specific website.
      4. The **Super User** role is the most powerful role and gives the user the ability to do anything to any website, as well as enable/disable plugins and set global system settings.

   2. **Adding a new website**

      To add a website, You must be logged into Matomo as a super user:

      1. Click on **Administration** to access the administration area, then under **Websites/Measurable** click on **Manage**. This page is used to create, update and delete websites.

      2. Click on **Add a new website** to create a new site in Matomo. The website form shows all the options you can specify.

         <aside>
          ➡️ This will work for non-cross domain tracking only, for cross-domain tracking you would need to add a website as an ‘alias’ one. See ‘Multiple websites tracking’ section below for more information

         </aside>

   3. **Multiple websites tracking**

      1. **Tracking one domain.**

         This is the standard use case. Matomo tracks the visits of one domain name with no subdomain, in a single Matomo website:

         ```jsx
         // Default Tracking code

         _paq.push(['setSiteId', 1]);

         _paq.push(['setTrackerUrl', u+'matomo.php']);

         _paq.push(['trackPageView']);
         ```

         <aside>
          ➡️ If you are tracking one specific subdomain, this default tracking code also works

         </aside>

      2. **Tracking one domain and its subdomains in the same website**

         To record users across the main domain name and any of its subdomains, we tell Matomo to share the cookies across all subdomains. **setCookieDomain()** is called in the Matomo tracking code on every related website:

         ```jsx
         _paq.push(['setSiteId', 1]);

         _paq.push(['setTrackerUrl', u+'matomo.php']);

         // Share the tracking cookie across
         // example.com and all of its subdomains

         _paq.push(['setCookieDomain', '*.example.com']);

         // Tell Matomo the website domain so that clicks on these domains
         // are not tracked as 'Outlinks'

         _paq.push(['setDomains', '*.example.com']);

         _paq.push(['trackPageView']);
         ```

      3. **Tracking subdirectories of a domain in separate websites**

         When tracking subdirectories of a domain in their own separate Matomo website, it is recommended to customise the tracking code to ensure optimal data accuracy and performance. For example, if your website offers a 'User profile' functionality, you may wish to track each user profile pages in a separate website in Matomo.

         - In the main domain homepage, you would use the default tracking code:

         ```jsx
         // idSite = X for the Homepage

         // In Administration > Websites for idSite=X,
         // the URL is set to `example.com/`

         _paq.push(['setSiteId', X]);

         _paq.push(['setTrackerUrl', u+'matomo.php']);

         _paq.push(['trackPageView']);
         ```

         - In the **example.com/user/MyUsername page** (and in every other user profile), you would construct calls to custom **setSiteId**, **setCookiePath** and **setDomains**:

         ```jsx
         // The idSite Y will be different from other user pages

         // In Administration > Websites for idSite=Y,
         // the URL is set to `example.com/user/MyUsername`

         _paq.push(['setSiteId', Y]);

         // Create the tracking cookie specifically in
         // `example.com/user/MyUsername`

         _paq.push(['setCookiePath', '/user/MyUsername']);

         // Tell Matomo the website domain so that clicks on other pages
         // (eg. /user/AnotherUsername) will be tracked as 'Outlinks'

         _paq.push(['setDomains', 'example.com/user/MyUsername']);

         _paq.push(['setTrackerUrl', u+'matomo.php']);

         _paq.push(['trackPageView']);
         ```

         <aside>
          ➡️ When tracking many subdirectories in separate websites, the function **setCookiePath** prevents the number of cookies to quickly increase and prevent browser from deleting some of the cookies. This ensures optimal data accuracy and improves performance for your users (fewer cookies are sent with each request).

         </aside>

   4. **Cross-domain tracking and roll-ups**

      When you want to group together the data and reports from multiple websites’ domain names into the same website in Matomo, you have two solutions:

      1. You can setup Cross Domain linking in Matomo to ensure that your visitors will be accurately tracked across domains into the same visit. How to setup cross-domain tracking:
         - **Configure your domain names as Alias URLs for your Matomo website.** Login to Matomo and click on Administration > Websites > Manage. Edit your website, and specify all your domain names in the Alias URLs field. There must be two or more domains for cross domain to work.

         - **Generate your JavaScript tracker code.** In Administration > Websites > Tracking Code, click on “Advanced: Show” link, then check the option “Enable Cross Domain linking” (If this checkbox is not clickable, please check you have defined at least two Alias URLs for this website). This will also automatically check the box “In the ‘Outlinks’ report, hide clicks to known alias URLs”.

         - **Check your generated JavaScript tracker code is valid.** In the generated Tracking code in Matomo you should see the following two lines:

           ```jsx
           _paq.push(["setDomains", ["*.domain1.com", "*.domain2.com"]]);
           _paq.push(["enableCrossDomainLinking"]);
           ```

         - **Paste this JavaScript tracker code into all your websites to be measured across domains**. In the example above, you need to add the JavaScript tracker code to domain1.com and domain2.com. It is important to add the code to all your domains specified as Alias URLs on your Matomo website.

         - **Check that the Cross Domain linking is working correctly.** Go to your domain1.com and click on a link to your domain2.com. If Cross Domain linking is enabled and working, the URL of domain2.com will contain a new parameter **&pk_vid=**. This **pk_vid** parameter will contain a string of data which includes the **Visitor ID**

      ii. Or you can create a new Roll-Up and group the websites together. Roll-up reporting lets you aggregate the reports of multiple websites you select into a Roll-Up. You can create an unlimited number of Roll-ups. You get unlimited number of websites for On-Premise installations and up to 30 websites for Cloud instances. **To create a Roll-Up, follow the steps below:**

      - Click on “All Websites” on the top right
      - Click on “Add a new website”, a pop up will appear
      - Click on “Roll-Up” to create a Roll-Up
      - Name your Roll-Up as desired
      - Choose the websites from the dropdown under “Source measurables” or search for a term and add all the websites which contains the search term
      - Configure the currency and time zone of your preference
      - Click on “Save”

   **e. How to import data from GA to Matomo:**

   <aside>
    ➡️ When you start a GA import in Matomo, a new website will be automatically created within Matomo for the imported data.

   **The import can’t go into an existing website in Matomo, and it cannot be merged later**

   </aside>

   There are 2 ways to import data:

   - Quick Connect with Google Analytics
   - Advanced Google OAuth client configuration
     - If you have multiple websites or high-traffic websites, the Advanced Google OAuth configuration is ideal. It allows for faster migration and the ability to import more data thanks to higher API limits.

   1. Follow the steps provided below for the Quick Connect method:
      - Navigate to the Google Analytics Import screen (go to Administration > System > Google Analytics Import).

      - Choose Quick connect as your way of importing.

      - Click the “Connect with Google Analytics” button (this opens a new tab).

        <aside>
          ➡️ **Note:** You may receive a warning from Google saying “Google hasn’t verified this app”. In this case, you can safely continue by clicking on “Advanced”, and then “Go to matomo.cloud (unsafe)”.

        </aside>

      - Select the Google Analytics properties you want to import.

      - Click the “Import properties” button.

        <aside>
          ➡️ **Note:** Once you click “Import properties”, Matomo will automatically create a new Matomo **website for each selected property**

        </aside>

      - To see your data, refresh the page and select the newly created Matomo website from the dropdown on the top left.
   2. For the OAuth method, follow [this guide](https://matomo.org/faq/general/set-up-google-analytics-import/)
   3. (?)3rd method (for self-hosted version of Matomo):
      - **Make sure you use the latest version of Matomo and the** [**Google Analytics Importer**](https://plugins.matomo.org/GoogleAnalyticsImporter) plugin
        - [Install the plugin](https://matomo.org/faq/plugins/faq_21/) mentioned above.
      - **Setup Google Analytics import in Matomo.** Follow the steps in the [“**Setting up the Google Analytics import**“](https://matomo.org/faq/general/set-up-google-analytics-import/) to get started. This authorizes your Matomo install to access your Google Analytics data.
      - **Schedule the Google Analytics import to run.** This step is covered in full in [“**Running the Google Analytics import**“](https://matomo.org/faq/general/running-the-google-analytics-import/).
      - **Embed the Matomo tracking code into your website.** Now that the new website has been created for the import, then you can use the Matomo JavaScript tracking code for this newly created website.
      - **Check that your website is now tracked in Matomo correctly.** Check you can see your own visits and other visitors in real-time (if you are not seeing data, [use this faq](https://matomo.org/faq/troubleshooting/faq_58/)).
      - **Update the Import Job and set the “End Date” to today’s date.** The importer will import the data for the set period. Remove old code snippets from the website which helped track to GA.

2. **Data Privacy:**

<aside>
➡️ List of [Matomo cookies, purposes and expiration time](https://matomo.org/faq/general/faq_146/). All of them are 1st party cookies

</aside>

1. **General recommendations. To be compliant with GDPR, a data subject must be able exercise the different rights below:**

   1. Right to be informed

      - If you are processing personal data, you need to inform users at the point of the data collection with a clear privacy notice. This privacy notice needs to include at a minimum:
        - the reasons why you are processing the personal data
        - for how long
        - who the different parties you are going to share them with are
        - a completed [privacy policy page](https://matomo.org/privacy-policy/).

   2. Right of access

      - If a visitor asks you to get access to her or his personal data, you have the responsibility to check her/his identity. This can be done by matching the requests email with the one you have in Matomo.

        <aside>
          ➡️ *Note that if you anonymize the personal data, then you cannot search for a data subject as it is not a personal data anymore.*

        </aside>

        - Go to Administration → Privacy → GDPR tools, and find the user by matching conditions. After you have verified each visit that belongs to the data subject you want to export the data for, click on **‘EXPORT SELECTED VISITS’** to pull out the data. This will download a file with all the necessary data which you can send the data subject by email.

   3. Right to erasure

      - In order to delete information of a given user, you will have to follow this procedure:
        - Click on Administration (the wheel logo at the top right of Matomo’s admin panel);
        - Click on “GDPR tools” under the Privacy category;
        - Search for a data subject by matching conditions;
        - Once selected, click on **‘DELETE SELECTED VISITS’**.

   4. Right to rectification

      - If you are presented with a request to rectify the data of a data subject, we recommend you to use the right to erasure instead. See the previous step for more information.

   5. Right to data portability

      - A user has the right to ask to get a copy of their personal data. Please first check their identity as described in “Right to access” step above.

        In order to exercise the following right:

        - Click on administration (the wheel logo at the top right of Matomo’s admin panel);
        - Click on “GDPR tools” under the Privacy category;
        - Search for a data subject by matching conditions;
        - Once found click on **‘EXPORT SELECTED VISITS’** and send the data to the user.

   6. Right to object

      - A user has to be able to object to the processing of their personal data. You can easily offer this feature by enabling Matomo’s opt-out feature.

        It consists of an iFrame that you can insert on a web page where users would expect to find it, most likely in your [privacy policy page](https://matomo.org/privacy-policy/).

        - Click on Administration (the wheel logo at the top right of Matomo’s admin panel)
        - Click on “Users Opt-out” under the Privacy category
        - Tweak the HTML code according to your website:
          - **backgroundColor**, a hexadecimal color string for example ‘ffffff’ or ‘ddd’;
          - **fontColor**, a hexadecimal color string for example ‘ffffff’ or ‘ddd’;
          - **fontSize**, a valid CSS font size for example 1.2em, 15pt, 15px or 50%;
          - **fontFamily**, a string containing only letters, space, or hyphen eg. ‘Lucida’, ‘Courier new’;
          - **language**, the language of the opt-out text, a two letter code eg. ‘en’ or ‘de’;
        - Copy/Paste it on your website where users expect to see it (for example, the privacy policy page);
        - Test that it is properly working.

      <aside>
       ➡️ Alternatively, you can use a 3rd party solution

      </aside>

   7. Right to withdraw consent

      - Under GDPR, if a user gave you their consent, you have to provide them a way to withdraw it. In order to remove her/his consent the user needs to perform a specific action, for example: clicking on a button “I do not want to be tracked anymore”.

        - [Learn more about how to setup the Matomo consent feature](https://developer.matomo.org/guides/tracking-consent).
        - You can also click on Administration (the wheel logo at the top right of Matomo’s backend), and then click on “Asking for consent” under the Privacy section.

        <aside>
          ➡️ Alternatively, can use 3rd party solution.

        </aside>

2. **Other procedures to follow(?):**

   1. For Matomo Cloud version:
      - Inform your visitors through [a clear privacy notice](https://matomo.org/blog/2018/04/how-should-i-write-my-privacy-notice-for-matomo-analytics-under-gdpr/) whenever you’re collecting personal data.
      - Inform your users in your [privacy policy](https://matomo.org/blog/2018/04/how-to-complete-your-privacy-policy-with-matomo-analytics-under-gdpr/) about what data you collect and how the data is used.
      - Make your team aware that you are using Matomo Analytics and [what data is being collected by your analytics platform](https://matomo.org/faq/general/faq_18254/).
      - Document your use of Matomo within your [information asset register](https://matomo.org/blog/2018/04/gdpr-how-to-fill-in-the-information-asset-register-when-using-matomo/).
   2. If self-hosting:
      - Apply our [security recommendations](https://matomo.org/docs/security-how-to/) in order to keep your Matomo data safe.
      - Check that you have a written contract with the company providing you the Matomo server or hosting which ensures [appropriate safeguards are provided](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/international-transfers/).
      - Include Matomo in your [data breach procedure](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/personal-data-breaches/).
      - Include Matomo in your [data privacy impact assessment (DPIA)](https://www.cnil.fr/en/guidelines-dpia), if applicable.

3. **Matomo offers two forms of consent:**

   1. **Cookie Consent:** This method prevents tracking cookies from being set until consent is gained. However, [less specific data will still be collected](https://matomo.org/faq/general/faq_156/) before cookie consent has been provided. After consent is given, data is tracked normally;

   2. **Tracking Consent:** With this method, nothing is tracked by Matomo until the user has consented. After consent is given, data is tracked nornally. This offers the highest level of privacy to users, but will likely result in missing or inaccurate tracking data for website owners.

   3. **“Cookie Consent” setup guide (using CookieBot):**

      - This mode can be used when personal data is not being tracked. If consent to use cookies is not given then Matomo will still track visitors without using cookies and provide a full range of metrics. However, when cookies are disabled, some data in Matomo will be less accurate:

        <aside>
          ➡️ Matomo uses cookies to store a unique visitor ID, used to recognize visitors from previous visits. When cookies are disabled, Matomo will still be able to determine unique visitors based on IP address and other footprints, but this will be inaccurate:

        1. Goals and Ecommerce conversions will be attributed to the channel used in the visit that converts
        2. Multi Attribution and Cohort reports won’t show data
        3. The following reports won’t display accurate data anymore, because all visits without cookie will be counted as if they were new visitors, making the report inaccurate:
           - Days since last visit
           - Visits by visit count
           - Visits to Conversion
           - Days to Conversion

        Cookies will only be used if consent for **Statistics** cookies was given in Cookiebot.

        </aside>

      - Setup:

        - Go to *Administration > Measurables > Tracking Code* in your Matomo dashboard, make sure the correct website is selected.

        - **Copy the tracking code shown in the Matomo dashboard** and paste it into a text editor. It should look similar to this:

          ```jsx
          <!-- Matomo -->

          <!-- SAMPLE CODE - DO NOT COPY THIS -->

          <!-- COPY THE TRACKING CODE FROM YOUR MATOMO DASHBOARD -->

          <script>

          var _paq = window._paq = window._paq || [];

          _paq.push(['trackPageView']);

          _paq.push(['enableLinkTracking']);

          (function() {

          var u="//matomo/";

          _paq.push(['setTrackerUrl', u+'matomo.php']);

          _paq.push(['setSiteId', '1']);

          })();

          </script>

          <script src="//matomo/matomo.js"></script>

          <!-- End Matomo Code -->
          ```

        - Add the line **\_paq.push(['requireCookieConsent']);** just before the first line starting with **\_paq.push**.

        - The resulting code should now look similar to this:

          ```jsx
          <!-- Matomo -->

          <!-- SAMPLE CODE - DO NOT COPY THIS -->

          <!-- COPY THE TRACKING CODE FROM YOUR MATOMO DASHBOARD -->

          <script>

          var _paq = window._paq = window._paq || [];

          _paq.push(['requireCookieConsent']);

          _paq.push(['trackPageView']);

          _paq.push(['enableLinkTracking']);

          (function() {

          var u="//matomo/";

          _paq.push(['setTrackerUrl', u+'matomo.php']);

          _paq.push(['setSiteId', '1']);

          })();

          </script>

          <script src="//matomo/matomo.js"></script>

          <!-- End Matomo Code -->
          ```

        - This code should now be added to all pages on your website directly before the tag, if you already have Matomo tracking code on the page then it should be replaced with this updated version.

      <aside>
       ➡️ If you are using Matomo Tag manager with cookie consent solution:

      - You can create a “Custom HTML” tag, and insert **\_paq.push(['requireCookieConsent']);** in this tag.
      - You would also need to create a Trigger on “DOM Ready” (**which will / needs to be executed first before the Pageview trigger**).
      - Then in your Custom HTML tag, set “Execute this tag when any of these triggers are triggered.” to “DOM Ready”.

      </aside>

   4. **“Consent to Track” setup guide (using CookieBot)**

      - If personal data is tracked, such as user identifiers or eCommerce orders, then this mode should be used. If consent for **Statistics** cookies is not given in Cookiebot then Matomo will not perform any tracking at all.
      - Setup:
        - Go to *Administration > Measurables > Tracking Code* in your Matomo dashboard, make sure the correct website is selected.

        - **Copy the tracking code shown in the Matomo dashboard** and paste it into a text editor. It should look similar to this:

          ```jsx
          <!-- Matomo -->

          <!-- SAMPLE CODE - DO NOT COPY THIS -->

          <!-- COPY THE TRACKING CODE FROM YOUR MATOMO DASHBOARD -->

          <script>

          var _paq = window._paq = window._paq || [];

          _paq.push(['trackPageView']);

          _paq.push(['enableLinkTracking']);

          (function() {

          var u="//matomo/";

          _paq.push(['setTrackerUrl', u+'matomo.php']);

          _paq.push(['setSiteId', '1']);

          })();

          </script>

          <script src="//matomo/matomo.js"></script>

          <!-- End Matomo Code -->
          ```

        - Add the line **\_paq.push(['requireConsent']);** just before the first line starting with **\_paq.push**.

        - The resulting code should now look similar to this:

          ```jsx
          <!-- Matomo -->

          <!-- SAMPLE CODE - DO NOT COPY THIS -->

          <!-- COPY THE TRACKING CODE FROM YOUR MATOMO DASHBOARD -->

          <script>

          var _paq = window._paq = window._paq || [];

          _paq.push(['requireConsent']);

          _paq.push(['trackPageView']);

          _paq.push(['enableLinkTracking']);

          (function() {

          var u="//matomo/";

          _paq.push(['setTrackerUrl', u+'matomo.php']);

          _paq.push(['setSiteId', '1']);

          })();

          </script>

          <script src="//matomo/matomo.js"></script>

          <!-- End Matomo Code -->
          ```

        - This code should now be added to all pages on your website directly before the tag, if you already have Matomo tracking code on the page then it should be replaced with this updated version.

      <aside>
       ➡️ Even if disabled totally, some cookies may sill be placed (functional, for security reasons):

      - **piwik_ignore** – When you exclude yourself from being tracked using the cookie method or using the iframe opt-out method, Matomo will create a cookie piwik_ignore set on the domain of your Matomo server;
      - **MATOMO_SESSID** – MATOMO_SESSID is a temporary short-lived cookie that provides a [*nonce*](https://en.wikipedia.org/wiki/Cryptographic_nonce) – basically a random number – which helps to prevent [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery) security issues while users opt-out of tracking;
      - **mtm_consent** and **mtm_consent_removed** – When you’re asking for consent before tracking visitors, these two cookies may be created: mtm_consent and mtm_consent_removed;
      - **\_pk_testcookie** – The \_pk_testcookie is only used to check whether the visitor’s browser supports cookies and is created without any identifier, and is also deleted shortly afterwards.

      </aside>

4. **Cookieless tracking:**

   1. To prevent cookies from ever being used **for (!)ALL WEBSITES**:

      - Log in to Matomo as a [super user](https://matomo.org/faq/general/faq_35/);

      - Go to “Administration -> Privacy -> Anonymize data” and enable the checkbox “Force tracking without cookies”.

        <aside>
          ➡️ **NOTE:** Enabling this option will automatically update the JavaScript tracker to ensure all trackers won’t use cookies. Additionally, Matomo will ignore all received tracking cookies on the server side.

        **NOTE:** Cookies will be disabled even when using the consent methods in Matomo tracker and calling for example the cookie consent methods won’t enable cookies.

        </aside>

   2. To prevent cookies from ever being used for **a dedicated website**:

      - If you have installed Matomo on your website with the [JavaScript tracking code](https://developer.matomo.org/guides/tracking-javascript-guide#finding-the-piwik-tracking-code), it is easy to disable tracking cookies **for a specific website**, by adding one line in the Matomo Javascript code.

      - Simply find the tracking code in your sites editor and look for the line that includes **\_paq.push(['trackPageView']);** and add the function **\_paq.push(['disableCookies']);** on the line before that. So afterwards that section of your code will look a little something like this:

        ```jsx
        [...]

        // Call disableCookies before calling trackPageView

        _paq.push(['disableCookies']);

        _paq.push(['trackPageView']);

        [...]
        ```

      <aside>
       ➡️ If you are using Matomo Tag manager without cookie consent solution:

      1. You can use a built-in feature that enables you to disable cookies. When setting up your Matomo configuration variable, make sure the **Disable Cookies** checkbox is enabled.
      2. When creating a Matomo Tag, you will see a Matomo Configuration setting, where you could add the previously created variable.

      </aside>

      <aside>
       ⬇️ **NOTE:** This alone isn’t sufficient for cookieless tracking setup. Refer to the next section to complete the setup

      </aside>

      - **How to use Matomo without banner and cookie consent:**

        As part of privacy legislation worldwide including [GDPR](https://matomo.org/gdpr-analytics/), CCPA, PECR, and [ePrivacy](https://matomo.org/blog/2017/01/new-proposed-eprivacy-regulation-piwik-might-not-need-tracking-consent-compared-google-analytics-co/), it is often required to display a cookie banner informing users about cookies, or consent must be obtained before tracking visitors’ data.

        **You can safely use Matomo without a consent mechanism as long as:**

        - The collected analytics data contains no personal data;
        - The collected data is only used for analysis and no other purpose;
        - The data is not shared or connected with data from other websites;
        - You provide accurate information about your data collection in a privacy policy.

        **Cookie banner can be disabled if you:**

        - Are with either total cookie less tracking or based on consent;
        - Easily let users opt-out;
        - Mention Matomo in your Privacy Policy.

        **Collection of personal data within Matomo is minimized.** If you follow all of these steps, it is likely that you won’t need to gain user consent for your use of analytics (steps to enable all that is mentioned below are [here](https://matomo.org/faq/new-to-piwik/how-do-i-use-matomo-analytics-without-consent-or-cookie-banner/)):

        - Disable Cookies;
        - Anonymise IP Address;
        - Anonymise referrer;
        - Exclude personal data from URLs and Page Titles;
        - Exclude personal data from Custom variables, Dimensions and Events;
        - Mask Personal Data in Heatmaps and Screen Recordings;
        - Exclude/Anonymize Ecommerce Order IDs:
          - Click **Anonymize data** within the **Privacy** menu on the Matomo **Settings** page;
          - Click **Anonymize Order ID** so a green tick is shown;
          - Click the big green **Save** button.
        - Do not enable User ID Features;
        - Only use collected data for analytics;
        - Only track users on a single site/application - do not track users across different websites;
        - Offer Opt-Out Mechanism – We recommend you [include the Matomo Opt-out form](https://matomo.org/faq/general/faq_20000/) within your Privacy Policy page;
        - Publish an updated Privacy Policy;
        - Can also [add Privacy Policy and Terms & Conditions links in Matomo](https://matomo.org/faq/how-do-i-display-links-to-my-privacy-policy-and-or-terms-conditions-to-people-who-view-matomo-reports/).
        - The [Do Not Track preference](https://en.wikipedia.org/wiki/Do_Not_Track) is an additional way users can tell all websites they would prefer not to be tracked.
          - Click the ***cog icon*** within the top menu to load the Matomo settings page.
          - Click **Users opt-out** menu item within the **Privacy** section of the main navigation on the left-hand side.
          - Scroll down to the **Support Do Not Track preference** section.
          - Click **Enable Do Not Track support (Recommended)** so a green bullet is shown.
          - Click the big green **Save** button.

5. Cookieless tracking based on consent

   1. If you would like to further customize the cookieless tracking, meaning to collect data based on cookies after user consented to, follow the guide (for CookieBot):
      - Add the consent manager code to your website.

      - To have the Matomo JavaScript tracker always use the visitor consent status provided by Cookiebot the following code should be added to the header of each website page beneath the Cookiebot code:

        ```jsx
        <script>

        var waitForTrackerCount = 0;

        function matomoWaitForTracker() {

        if (typeof _paq === 'undefined' || typeof Cookiebot === 'undefined') {

        if (waitForTrackerCount < 40) {

        setTimeout(matomoWaitForTracker, 250);

        waitForTrackerCount++;

        return;

        }

        } else {

        window.addEventListener('CookiebotOnAccept', function (e) {

        consentSet();

        });

        window.addEventListener('CookiebotOnDecline', function (e) {

        consentSet();

        })

        }

        }

        function consentSet() {

        if (Cookiebot.consent.statistics) {

        _paq.push(['setCookieConsentGiven']);

        _paq.push(['setConsentGiven']);

        } else {

        _paq.push(['forgetCookieConsentGiven']);

        _paq.push(['forgetConsentGiven']);

        }

        }

        document.addEventListener('DOMContentLoaded', matomoWaitForTracker());

        </script>
        ```

        <aside>
          ➡️ Matomo will only track visitors if they have given the Cookiebot **‘Statistics’** consent.

        </aside>

6. **Data retention**

   Within Matomo, there are essentially two types of data:

   1. **Raw Data:** This shows you all of the information about a single visit to a website and is typically accessed through the [visit log](https://matomo.org/docs/real-time/#visits-log). It includes the source, available user data, and all on-site activity within a visit. This information is also used when [creating new segment reports](https://matomo.org/docs/segmentation/).
   2. **Report Data:** This is the aggregated data that is compiled from the raw data to create reports which show information about groups of users for a specific metric. An example would be the number of visits from a certain country on a specific date. This is the most commonly used type of data for reviewing your website trends over time.

   <aside>
    ➡️ Matomo enables you to set different data retention policies for each type of data to enhance the privacy of your users.

   → If you are using [Matomo Cloud](https://matomo.org/matomo-cloud/) then you can keep an unlimited amount of *report data*, but the amount of *raw data* you can keep is limited in accordance with your plan.
   → However, if you are using the [Matomo On-Premise](https://matomo.org/matomo-on-premise/) or [Matomo for WordPress](https://wordpress.org/plugins/matomo/) version then you can choose to keep both types of data indefinitely.

   </aside>

   1. As raw data is inherently more personal and can be used to identify the actions of a single user, it is common to delete this type of data more frequently than aggregate report data.

      - Click **Anonymize data** within the Privacy menu on the Matomo **Settings** page.
      - Scroll down to the **Regularly delete old raw data** section.
      - Click **Regularly delete old raw data from the database** so a green tick is shown.
      - Enter a number of days into the **Delete logs older than (days)** text field. For reference: one year is equal to 365 days and two years is equal to 730 days.
      - Click the big green **Save** button.

      <aside>
       ➡️ To anonymize previously tracked raw data, follow these steps:

      - Login to Matomo as a Super User
      - Go to Administration > Privacy > Anonymize data.
      - In the section “Anonymize previously tracked raw data” you can configure a one-off data anonymisation process to run on data you have tracked in the past.
      - Choose to anonymise data for one **website**, or for all websites.
      - Choose the **start date and end date** to anonymize data for
      - Choose **which visit or action data column** to anonymize. (IP, UserID, Location, visits and action columns (values in some cases won’t be anonymised but set to default values)). Process can take a long time

      </aside>

   ii. Report data is core to the Matomo experience and as such it is possible to keep reports indefinitely. The main reason to remove aggregated data is if you no longer need access, or if the data is taking up space on your server:

   - Click **Anonymize data** within the Privacy menu on the Matomo **Settings** page.
   - Scroll down to the **Delete old aggregated report data** section.
   - Click **Regularly delete old reports from the database** so a green tick is shown.
   - Enter a number of days into the **Delete logs older than (months)** text field.
   - It is generally best to check the box to **Keep basic metrics** unless you have a reason not to. This feature retains data that cannot be associated with personal data i.e. numeric metrics without labels attached.
   - Select the reports you would like to **Keep all data for**.
   - Click the big green **Save** button and the remaining data will be deleted regularly.

7. **Other features & additional reports**

   1. **A/B tests**
      1. **Prerequisites:** A/B Testing is a premium feature which is included in [Cloud-hosted Business plan](https://matomo.org/hosting/), or you can [purchase it on the Matomo Marketplace](https://plugins.matomo.org/AbTesting) if you [self host Matomo On-Premise](https://matomo.org/what-is-on-premise/).

      2. **Management:** To get to the “Manage Experiments” screen, click on the user icon in the top right. There will be a new menu item “Experiments” in the left menu. They can be edited by anyone having at least ‘Write’ or ‘Admin’ access for a specific website.

      3. **General experiment setup workflow in Matomo:**

         - To create an experiment, click on “Create new experiment” in the bottom left. The form will ask you to enter some basic information to get you started with your experiment quickly.

         - In case you want to experiment and compare the performance of different pages URLs, you can create your experiment where you specify a Redirect Page URL for each variation. When you create your experiment, under the section “Redirects”, for each variation (including the “Original” variation) you can enter the Page URL to redirect to and test.

           <aside>
             ➡️ When you create an experiment using “Redirect URLs”, please make sure to include the Matomo Tracking code on all your pages including on the Redirect URLs pages

           </aside>

         - To start your experiment, click on “Embed code” and embed the displayed code into your website, app, server or campaign. The experiment will automatically start running as soon as the first user enters the experiment.

         - To mark an experiment as finished, either click on the link “Finish experiment” on the top of your experiment report page (in the experiment summary), or click “Finish experiment” when editing the experiment in the “Manage experiments” section. **Once you have finished your experiment, you should remove all code that is related to this experiment from your website or app.**

           <aside>
             ➡️ In the left menu click “Experiments” and then select an experiment of your choice. The reporting UI displays the currently running experiments as well as the finished experiments

           </aside>

      4. **Implementation of A/B testing code**:

         <aside>
          ➡️ The [A/B Testing plugin](https://www.ab-tests.net/) directly adds the JavaScript A/B testing framework to your Matomo JavaScript tracker file /matomo.js and is therefore loaded automatically with the [Matomo JavaScript Tracking Code](https://developer.matomo.org/guides/tracking-javascript-guide).

         To check whether this works by default for you, login into Matomo as a Super User, go to Administration, and open the "System Check" report. If the System Check displays a warning for "Writable Matomo.js" (should be writable), go to [full documentation](https://developer.matomo.org/guides/ab-tests/browser) to resolve the issue, otherwise no action is needed.

         </aside>

         - To prevent any flickering / flashing of content when you run your experiments, you need to make sure to load the matomo.js tracker file as early as possible. Edit your JavaScript tracking code as follows:

           - Move the Matomo Tracking Code that loads the matomo.js file into the HTML <head>

           - Load the file synchronously instead of asynchronously by Removing the lines containing:

             ```jsx

             var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
             g.type='text/javascript';
             g.async=true;
             g.src=u+'matomo.js';
             s.parentNode.insertBefore(g,s);
             ```

           - Add the following line after the closing **</script>** element:

             ```jsx
             <script type="text/javascript" src="//$yourPiwikDomain/matomo.js"></script>
             ```

           - Your JavaScript tracker code should look like this:

             ```jsx
             <head>

             <script type="text/javascript">

             var _paq = window._paq = window._paq || [];

             // [...]

             (function() {

             var u = "//$yourPiwikDomain/";

             _paq.push(['setTrackerUrl', u+'matomo.php']);

             _paq.push(['setSiteId', 'X']);

             })();

             </script>

             <script type="text/javascript" src="//$yourMatomoDomain/matomo.js">
             ```

         - When creating an experiment in your Matomo, the A/B testing plugin will generate for you the JavaScript code that will run your experiment and that you need to embed in your pages.

           - The embedded experiment code should be placed before your page view is tracked, in the head section, and after the DOM is ready.

             <aside>
               ➡️ **NOTE:** Do not put it into any tag manager.

             </aside>

           - Example and anatomy of the code:

             ```jsx
             var _paq = window._paq = window._paq || [];

             _paq.push(['AbTesting::create', {

             // [...]

             percentage: 100,

             startDateTime: '2017/08/25 00:00:00 UTC',

             endDateTime: '2020/05/21 23:59:59 UTC',

             trigger: function () {

             if (isLoggedIn && userAge < 50) {

             return true;

             }

             return false;

             },

             matomoTracker: Matomo.getAsyncTracker(matomoUrl, matomoSiteId),

             variations: [

             // [...]

             {

             name: 'VariationA',

             percentage: 40,

             activate: function(event) {}

             }

             ]

             }]);
             ```

             - name: name of the variation of the experiment
             - variations: The list of different variations you want to compare. Experiments can be created for more than just two variations (A/B).
             - includedTargets: Specifies on which target pages the experiment is supposed to be activated. For an experiment to be activated, all rules need to match (logical AND) and none of the excluded targets is allowed to match.
             - percentage - The percentage of how many of your users should take part in this experiment. By default, 100% of your users will participate in your experiment and see either the original version or any of your variations.
             - startDateTime - If configured, the experiment will not be activated until the specified start time.
             - endDateTime - If configured, the experiment will no longer be activated after the specified end time.
             - trigger - The trigger function allows you to further restrict which of your visitors will participate in your experiment. For example if you want to run the experiment only for visitors from a specific country or only want to activate the experiment on a certain type of pages, you can use this method to customize who will participate in this experiment.
             - matomoTracker - Lets you set a Matomo tracker instance if you track your data [into multiple Matomo instances](https://developer.matomo.org/guides/tracking-javascript-guide#multiple-piwik-trackers) and wish your experiments to be only tracked into one specific Matomo instance.
             - variation.percentage - By default, each variation gets the same amount of traffic but you can allocate more or less traffic to individual variations. You don't have to configure a percentage on all variations. If a percentage is only specified for a few variations, all other variations will share the remaining percentage equally. For example, if you specify VariationA should get 40%, then the original version and VariationB will share the remaining 60% and be seen by 30% of your traffic each. We recommend not to assign more than 100% across all of your variations.

         - For example, if you want to compare different color buttons, you can implement the **‘activate’** method as follows:

           ```jsx
           variations: [{

           name: 'blue',

           activate: function(event) {

           document.getElementById('btn').style.color = '#0000ff';

           }

           },

           {

           name: 'red',

           activate: function(event) {

           document.getElementById('btn').style.color = '#ff0000';

           }

           }]
           ```

           Within the activate method, the **‘this’** context is within your variation. This means you can access the name of your variation via ‘**this.name’**.

           An event is passed to the **‘activate’** method which lets you for example:

           - access the instance of your experiment via **‘event.experiment’**;
           - redirect users via **‘event.redirect(url)’;**
           - define a function that is supposed to be executed as soon as the DOM is ready via **‘event.onReady(callback)’**.

      5. **Testing:**

         - Testing variations can be cumbersome because variations are activated randomly, and you always get to see the same variation. To test a specific variation you can append a URL parameter **?pk_ab_test=$variationName**.

         - Should you not want to run any A/B test for a while without needing to remove all the already embedded experiments from your website you can run execute the following code:

           ```jsx
           // works from A/B testing 3.2.18

           var _paq = window._paq = window._paq || [];

           _paq.push(['AbTesting::disable']);
           ```

      6. **A single-page application** is different from a usual website as there is no regular new page load, and Matomo cannot detect automatically when a new page is viewed. This means you need to let Matomo know whenever the URL and the page title changes and embed the A/B testing code again. You can do this using the methods **setCustomUrl**, **setDocumentTitle** and **AbTesting::create** like this:

         ```jsx
         window.addEventListener('pathchange', function() {

         var _paq = window._paq = window._paq || [];

         _paq.push(['setCustomUrl', window.location.pathname]);

         _paq.push(['setDocumentTitle', document.title]);

         _paq.push(['AbTesting::create', {

         name: 'theExperimentName',

         includedTargets: [{"attribute":"url","type":"starts_with","value":"http:\/\/www.example.org","inverted":"0"}],

         excludedTargets: [],

         variations: [

         {

         name: 'original',

         activate: function (event) {

         // usually nothing needs to be done here

         }

         },

         {

         name: 'blue',

         activate: function(event) {

         // eg $('#btn').attr('style', 'color: ' + this.name + ';');

         }

         }

         ]

         }]);

         _paq.push(['trackPageView']);

         });
         ```

   b. **Heatmaps and session recordings**: tracks interactions like clicks, mouse movements, scrolls, form interactions and page changes. These interactions can be afterwards replayed in a video or visualized in a heatmap, so you can find out what your visitors are really looking for. Before your users mouse movements will be recorded and your page heatmaps will be generated, you need to create a Heatmap.

   1. To get to the “Manage Heatmaps” screen, click either in the reporting or in the administration menu on “Heatmaps” and then “Manage”.
   2. To create a heatmap, click on “Create new heatmap” in the bottom left. To edit a heatmap, simply click on the “edit” icon next to the name of a previously created heatmap.
   3. Simply input the name for the heatmap and choose on which target page the heatmap should be generated for. To do this, you can choose between “URL”, “URL path”, “URL parameter” attributes and comparisons like “equals”, “starts with”, “contains”, “matches the regular expression”.

   <aside>
    ➡️ Heatmaps and session recordings reports:

   Go to Matomo. In the left menu click “Heatmaps” and then select a Heatmap report of your choice. There are several reports within: ‘click map’, ‘mouse move’, ‘scroll map’, and ‘above the fold’.

   </aside>

   c. **SEO Web Vitals feature** is exclusive to Matomo **On-Premise** and is not available in Matomo Cloud currently.

   1. **Prerequisites:**
      - SEO Web Vitals plugin for Matomo, [available for purchase on the Matomo Marketplace](https://plugins.matomo.org/SEOWebVitals) as a yearly subscription.
      - Any page you want to monitor must be fully public, [connected to the internet](https://matomo.org/faq/troubleshooting/faq_16646/) and crawlable by search engines. Typically, this should already be the case if you are aiming to optimise a page for better results in search.
      - Your page will need to have a valid SSL certificate enabled.
      - The final prerequisite is that any pages you want to measure must receive at least some regular visitors. This is because the data for your SEO Web Vitals are collected from visits to your website over 28 days.
   2. **Configuration**: Within the [main navigation menu](https://matomo.org/docs/matomo-tour/#main-navigation-3) on the left-hand side of your Matomo instance, click **Acquisition** to reveal the sub-menu, and then click the **SEO Web Vitals** menu item. Configure [the report](https://matomo.org/faq/reports/configure-the-seo-web-vitals-feature/').

   <aside>
    ➡️ **To access the report**, within the main navigation menu on the left-hand side of your Matomo instance click on the **Acquisition** tab and then click on the **SEO Web Vitals** menu item. Within this section, the report data is presented in table format and summarises the core metrics which make up your SEO Web Vitals:

   - Page Speed Score. This score is calculated from the rest of the metrics within this section and provides a simple indication of whether your pages are considered fast, average or slow. If you only want to look at a single metric to understand your page performance, it should be this one. Good is >90, Medium is 50 to 90.
   - First Contentful Paint (FCP). Measures the time until the browser can render the first piece of content after a user has navigated to your page. Up to 1.8sec is good.
   - Final Input Delay (FID). Metric measures the time it takes between the first time a visitor interacts with your page and the time for the resulting action to occur within the browser. This includes things like clicking on links and form fields, but not simply scrolling through your page. Good is up to 100ms.
   - Last Contentful Paint (LCP). Metric is related to the loading performance of your page and is defined as the time at which the largest text or image is painted or rendered on the screen. Good is up to 2.5 sec.
   - Cumulative Layout Shift (CLS). Metric measures the visual stability of your page while it is loading. Essentially it tracks the movement of elements that are currently visible on your page while loading. The CLS metric is based on a formula that calculates the size of any objects that move against the distance they move upon refresh. Good is a score of 0.1 or less.

   </aside>

   d. **Users Flow** is a premium feature which is included in all our [Cloud-hosted plans](https://matomo.org/hosting/), or you can [purchase it on the Matomo Marketplace](https://plugins.matomo.org/UsersFlow) if you [self host Matomo On-Premise](https://matomo.org/what-is-on-premise/). It shows you a visual representation of the most popular paths your users or visitors took through your website or app.

   1. Go to Matomo. In the menu click “Behaviour” and then “Users Flow”. You will see a visualization of the most popular pages and the paths your users took over several steps.
   2. In the top left you can adjust the report to show more or less details and to change the number of actions per interaction step.
   3. To analyze more Users Flow reports click in the menu on “Actions” and then “Top Paths”. In a glance you will see which paths your users take most often.

   <aside>
    ➡️ The “Overview” report lets you investigate the visitor engagement, for example after how many interactions your visitors drop off. When you click on a row, you can see which pages they visited most often at a particular interaction step, and where they went to from there.

   </aside>

   e. **The Transitions Plugin** gives you a report that shows the things your visitors did directly before and after viewing a certain page.

   1. You can launch it from the pages and page titles reports (*Behaviour > Pages* and *Behaviour > Page Titles*). When you move your mouse over a row of the table, two icons are shown. Click the X icon to open Transitions for this row:
      - **In the center**, you see general statistics about the page you launched Transitions on.

        - The first number is the number of pageviews for this specific page. Hover the number to see the share of all pageviews. You can also hover the other numbers to see the share of the groups.

        <aside>
          ➡️ On the sides of the box in the center, you see what visitors did directly before and after visiting the page in the center. *The height of the connections to the box in the center is proportional to the amount of traffic that took this route.*

        </aside>

      - **On the left side**, you can see where users came from:

        - *From Internal Pages* means that visitors came to the page in the center from other pages on your website.
        - The group *From Search Engines* shows how many people came from external search engines like Google directly to the page in the center.
        - *From Websites* shows which external websites linked directly to the page in the center.
        - *From Internal Searches* lists the keywords that your visitors searched for on your Internal Search engine, and then clicked to the page
        - The group *Direct Entries* shows visits that started on this page, i.e. the visitor used the page as a landing page.

      - **The right side** shows what users did after visiting the page in the center:

        - *To Internal Pages* means that visitors went to a different page on your website after their visit to the page in the center.
        - *Internal Searches* lists all the keywords that visitors started searching for, when they were on the page in the center.
        - When people click a download or outlink on the page, this is shown in the groups *Downloads* and *Outlinks.*
        - The group *Exits* shows visits that ended on this page, i.e. no more actions were tracked for the visitor.

   f. **Crash Analytics** provides insights into what’s failing in your website or application. Every time an unexpected error occurs it is logged in Matomo, giving you better insight into your users’ experience. Available as an extension on [matomo.org](http://matomo.org).

   g. **The Visits in Real-time report** is available under Visitors > Real-time. The Visits in Real-time report refreshes every 5 seconds, and displays new visits (or existing visitors that view a new page) at the top of list with a fade-in effect. For each visitor, you can see all of their attributes:

   - date
   - number of actions
   - time spent on the site
   - country
   - browser
   - operating system
   - whether the visitor is new or a returning one
   - the referrer used to access your site (Search engine & keyword, Campaign, or Referrer website)
   - whether the visitor reached a goal

   h. To open the **Visits Log** click on the reporting menu Visitor > Visits Log. The Visits Log is a tool that allows you to see all the visits on your site, and browse through these visits to check on individual user sessions.

   1. The Visitors Overview page provides a high-level summary of your website’s visitor numbers and engagement. You can access this page within the Matomo dashboard by clicking the **Visitors** menu item in the main navigation and then clicking on **Overview:**
      - The top section provides a row evolution chart that enables you to see how visits metrics are trending over time. The default metric displayed for this chart is **Visits**. It is possible to change which metrics are displayed by clicking on the ***line chart icon.***
      - The **Visits Overview** section on the second half of the **Overview** page shows a collection of [sparkline summaries](https://matomo.org/faq/reports/graphs-and-visualisations-in-matomo/#sparkline-summary-cards) which provide snapshots of key visitor metrics over your selected date range.

   j. **Creating custom reports, or** **Dashboards**: Whenever there is a unique collection of reports you need to check regularly, it is worth considering creating a dashboard. The majority of these settings are available through the ‘**dashboard**’ menu:

   - Go to the **Dashboard** section in the main navigation.
   - Click the **Dashboard** button.
   - Click **Create new dashboard** to bring up the dashboard creation popup.
   - Type a descriptive name in the field that pops up.
   - Choose between an **Empty dashboard** (recommended) or the default dashboard.
   - Click **OK** and then **Add A Widget** to load the widget selection menu and get started. This menu area lists all of the available widgets you can add to your dashboard.
     - To manage existing widgets within your dashboard, hover your mouse above the top right of the widget card to bring up the **Widget Menu (Refresh, Minimize, Maximize, Close).**
   - While on your dashboard page, click the **Dashboard** button. This will bring up the dashboard menu where you will see a **Manage dashboard** section at the bottom. Within this section, there is a **change dashboard layout** button which allows you to alter the number and width of columns on the page.

   k. **Multi attribution models**: if your website or app has Ecommerce enabled, you will automatically be able to view the attribution for orders in your shop:

   - Log in to your Matomo, and click in the left reporting menu on “Goals” and then “Multi Attribution”.
   - On this page, you can select the goal you want to see the channel attribution for.
   - The report lets you select how many days prior a conversion or purchase you want to attribute, and you can select various attribution models to compare.

   l. **Page Overlay shows analytics data directly on your website.** By doing this, it takes you closer the experience of your visitors and helps you understand traffic patterns.

   - Page Overlay can be launched from the rows of the Behaviour > Pages reports.
   - Just move your mouse over the page you want to see the Overlay for and click the bubble icon. It will open Page Overlay in a new tab.
   - Page Overlay displays the actual website and puts bubbles next to the links on the page that show how many visitors clicked the link, **but not in real time.**
