# My och Linn

![screenshot of the site on different devices](https://res.cloudinary.com/ivanprojects/image/upload/v1621281558/ms4/Screenshot_2021-05-17_at_21.54.01_jvdig0.png)

# Project Description

“My & Linn” is an online jewelry store which sells handcrafted & unique pieces, specialising in Silver. The pieces are made in Stockholm, Sweden by a family run business led by two sisters who are the head silversmiths My & Linn Johansson. 

Below is a live link to the site which is hosted on Heroku.
[HERE](https://myochlinn.herokuapp.com/)

## Table Of Contents

1. [Project Goals](#project-goals)
2. [Target Audience](#target-audience)
3. [UX Design](#ux-design)
    - [Strategy](#strategy)
    - [User Stories](#user-stories)
    - [Scope](#scope)
    - [Skeleton](#skeleton)
    - [Wire frames](#wire-frames)
    - [Surface](#surface)
4. [Design Choices](#design-choices)
    - [Typography](#typography)
    - [Color](#color)
    - [Imagery](#imagery)
5. [Information Architecture](#information-architecture)
6. [Existing Features](#existing-features)
7. [Features Left To Implement](#features-left-to-implement)
8. [Technologies Used](#technologies-used)
9. [Testing](#testing)
10. [Deployment](#deployment)
11. [Credits](#credits)

-----

## Project Goals

The goals of this project are to provide a place for customers to view, buy, compare the pieces available to purchase. It is also meant to be a HUB for clients to read blog posts & leave reviews on products amongst other things.

-----

## Target Audience

-   Families
-   Women of all ages.
-   Men 20yrs and above.
-   Influencers & celebrities.

-----

## UX Design

### Strategy

This site is at the request of client “My & Linn” who are a family owned jewelers looking to increase their online presence, make it easier for their customers to see and buy their products and increase business in general.

The aim was to create a website that will offer a very similar but also unique experience when compared to competitors. Customers should feel like they are using a smooth, reliable and professional site while also benefiting from the boutique and more personal feeling of the company.



### User Stories


| User Story Number | As A/An      | I should be able to...                                                         | So that I can ...                                                                                                    |
|-------------------|--------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| 1                 | Site Owner   | Add products                                                                   | Have new Items available for purchase on the site.                                                                   |
| 2                 | Site Owner   | Delete products                                                                | Have correct available stock information on the site.                                                                |
| 3                 | Site Owner   | Edit products                                                                  | Change & update relevant stock information.                                                                          |
| 4                 | Site Owner   | Add, modify & delete blog posts                                                | Keep the blog section of the site fresh                                                                              |
| 5                 | Site Owner   | View a blog on the site with relevant tips, advice and interesting content     | Add value to the website and brand as a whole                                                                        |
| 6                 | Site Owner   | Understand the purpose of the site                                             | Decide whether I want to invest my time into it.                                                                     |
| 7                 | Site Owner   | Site to be readable on all screen sizes.                                       | Shop on the site no matter which device I am using.                                                                  |
| 8                 | Site Visitor | View all available products                                                    | See which potential products I can purchase                                                                          |
| 9                 | Site Visitor | View a specific category of products                                           | Find a specific type of jewelry without having the inconvenience of seeing other categories I know I do not want     |
| 10                | Site Visitor | See individual product details                                                 | Learn more about the specific product                                                                                |
| 11                | Site Visitor | Easily see special offers/exclusive items                                      | Take advantage of temporary offers and products                                                                      |
| 12                | Site Visitor | See total shopping bag information at any time                                 | Control how much I am spending                                                                                       |
| 13                | Site Visitor | Search for product by words in name or description                             | Find a specific product                                                                                              |
| 14                | Site Visitor | See on search results, what I searched for and number of results found         | Reference the specific word I searched for and see how many items are matching the search                            |
| 15                | Site Visitor | View items in basket with short description of each                            | See which products I am thinking about purchasing and be reminded of why I want to purchase them                     |
| 16                | Site Visitor | Delete or change quantity of items in basket                                   | Easily change my mind or add/remove quantities of the same product without having to go to the specific product page |
| 17                | Site Visitor | Easily see and choose size/colour/quantity to purchase                         | Purchase with the specification I am comfortable with                                                                |
| 18                | Site Visitor | View information on how to care for product on product page                    | Keep the product in good condition for a long time                                                                   |
| 19                | Site Visitor | View a size guide for relevant products                                        | Feel sure about which size is best for me                                                                            |
| 20                | Site Visitor | Learn more about the business & their values from the about page               | Feel more comfortable buying from the company                                                                        |
| 21                | Site Visitor | Have easy access to a contact page                                             | Have an easy way to contact the company should I have any feedback or comments to make.                              |
| 22                | Site Visitor | Easily find out delivery information                                           | Easily see how long it will take to receive my product                                                               |
| 24                | Site Visitor | Find an FAQ section                                                            | Quickly find answers to common questions.                                                                            |
| 25                | Customer     | Easily enter my payment details                                                | Have a smooth payment experience                                                                                     |
| 26                | Customer     | See & feel that the payment process is secure                                  | Feel comfortable putting my payment information on the site                                                          |
| 27                | Customer     | See an order confirmation after payment process is complete                    | Be sure that the order has gone through                                                                              |
| 28                | Customer     | Receive email confirmation of order after website checkout process is complete | Have my own copy of an order confirmation and can relay back to this for relevant information.                       |
| 29                | Customer     | Easily be able to register an account                                          | Take advantage of benefits of having an account on the site                                                          |
| 30                | Customer     | Receive email confirmation of my account registration                          | Be sure that the registration process has gone through                                                               |
| 31                | Customer     | Easy access to the log in/out functionality at all times                       | Easily log in or out of my account at any point when on the website.                                                 |
| 32                | Customer     | Recover my password in case i forget                                           | Easily create now password and continue to shop on website                                                           |

### Scope

Based the user stories mentioned the features to be included in the project as well as their implementation schedule/priority are listed below. Also included are a list of features that will be left for later implementation.

#### Minimum Viable Product/Sprint 1:
- View, Add, Edit and Delete Products
- View products by category
- See individual product details and easily see and choose size/colour/quantity to purchase
- View items in basket with short description of each and delete or change quantity of items in basket
- Search for product by words in name or description
- See total quantity in bag at any time
- On a safe a secure checkout page, be able to enter payment details, see a confirmation page after payment & receive a payment/order confirmation email

#### Sprint 2:
- See on search results, what I searched for and number of results found.
- Easily be able to register an account
- Receive email confirmation of my account registration
- Easy access to the log in/out functionality at all times
- Recover my password in case i forget
- Add, modify & delete blog posts
- View a blog on the site with relevant tips, advice and interesting content

#### Sprint: 3:
- Find an FAQ section
- Easily find out delivery information
- Have easy access to a contact page
- Learn more about the business & their values from the about page
- View information on how to care for product on product detail page
- View a size guide for relevant products

#### Sprint 4:
- Testing & Debugging

### Skeleton

Wire frames were created to ensure that initial design and structure ideas actually worked and were realistic but also in keeping with UI & UX design principles.

### Wire frames

#### HOME/INDEX PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281547/ms4/Screenshot_2021-05-17_at_21.37.29_qtynqt.png)


#### ABOUT PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281548/ms4/Screenshot_2021-05-17_at_21.37.36_wibmz2.png)


#### CONTACT PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281548/ms4/Screenshot_2021-05-17_at_21.37.42_pwqdkh.png)

#### LOGIN PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281547/ms4/Screenshot_2021-05-17_at_21.38.05_c2tnry.png)


#### REGISTER PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281548/ms4/Screenshot_2021-05-17_at_21.38.21_bt92gv.png)

#### PROFILE PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281545/ms4/Screenshot_2021-05-17_at_21.39.14_nwu4ec.png)


#### PRODUCTS PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281546/ms4/Screenshot_2021-05-17_at_21.38.29_pu6jfd.png)


#### PRODUCT DETAIL PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281546/ms4/Screenshot_2021-05-17_at_21.38.36_kxe5ux.png)


#### CHECKOUT PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281546/ms4/Screenshot_2021-05-17_at_21.38.54_krulbq.png)


#### BASKET PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281547/ms4/Screenshot_2021-05-17_at_21.38.44_kuotvh.png)


#### FAQ/SUPPORT PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281547/ms4/Screenshot_2021-05-17_at_21.37.56_ikkn6r.png)


#### ORDER CONFIRMATION PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281545/ms4/Screenshot_2021-05-17_at_21.39.07_fyjxfb.png)


#### BLOG PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281545/ms4/Screenshot_2021-05-17_at_21.39.21_hlhsms.png)


#### ADD/EDIT BLOG POST/PRODUCT PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281545/ms4/Screenshot_2021-05-17_at_21.39.37_yjy4am.png)


#### BLOG DETAIL PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621281546/ms4/Screenshot_2021-05-17_at_21.38.36_kxe5ux.png)


### Surface

The structure and general feel of the site has been decided & at this point the focus was on deciding on the right colour palette, typography, animations and other design elements. Ideas & concepts were formed in tandem meaning that all design elements were thought about when deciding each specific element. This aided in creating a total look/feeling of the site with everything working well together.

The design choices also needed to reinforce some meaning or value & just have real purpose, the meaning/value/purpose comes from the user stories and the site’s general aims, these were always referred to when contemplating the design elements. This process aids in the creation of a semantic, concise and easy to use site.


## Design Choices

### Typography

Three main fonts were used for this site. The aims were to find a font to use as a logo for the brand and site & an interesting font that was flexible while still being unique.

To these aims we decided on firstly “Stanley” which is a stencil display typeface by Jeremie Gauthier. It is rounded in part but also still rectangular which keeps good readability. It is also quite contemporary and unique. This was chosen to be the logo font.

The second font chosen is called Emberly. This was chosen to be the main go-to font family for the site. It is an incredibly flexible typeface with 54 styles spread over 3 widths. Throughout the site, the main font style used is “Emberly Narrow” for titles, headers and important text. The font family is generally quite traditional serif but the flexibility allows for a more unique flavour. The Narrow style used in the site headers and important text is quite condensed, the letters do not have much space in between them so it was at some points necessary to increase the letter spacing to increase readability.

The third font and main font for general text throughout the site is one of the default fonts 'Lucida Sans'. This font works well as a cleaner looking reading font that offers more clarity to users eyes. It works well with the two other fonts and forms an ideal trio of fonts that bring out the best of each others features.

The @fontface CSS rule was used to include these custom fonts into the project after they were included in their own fonts folder within the static file directory.


![screenshot of Stanley](https://res.cloudinary.com/ivanprojects/image/upload/v1621281789/ms4/Screenshot_2021-05-13_at_21.19.28_m1kevl.png)

![screenshot of Emberly](https://res.cloudinary.com/ivanprojects/image/upload/v1621281634/ms4/Screenshot_2021-05-13_at_21.18.51_gdg6s5.png)

### Color

The colour palette for the site was carefully considered since competitor research showed a massive lean towards either white or beige for main colour choices. The need to be unique meant that we tried to choose colours that were different from the ones commonly found but also took into account the content that would be on the site, the products and the general layout of the site. With that in mind, a combination of whites into greys and eventually black was chosen.

One of the main reasons these colours were chosen was that the site content and more specifically the pictures were to be quite colourful and the thought was to give the pictures the right backdrop to stand out as much as possible. The pictures showcasing the products on sale was the priority. The colours also allow for good contrast throughout the site.


![screenshot of color palette](https://res.cloudinary.com/ivanprojects/image/upload/v1621285641/ms4/Screenshot_2021-05-17_at_22.03.40_h1fulr.png)

### Imagery

The imagery was chosen with the aim of inspiring customers, standing out and giving the wow factor. As mentioned above the general site colour palette really allows the imagery to take center stage.

## Information Architecture

In development i used the Django default SQLite database, with deployment to Heroku, a PostgresSQL database was used.

### Data Models:
The data is structured into 9 apps which house 8 data models.

#### Home app
Displays home page.

#### About app
Displays the about page

#### Bag app
Displays shopping bag page and controls the update and delete functionality of the shopping bag.

#### Blog app
Handles blog pages and CRUD operations.

Post Model:
Holds data for each blog post
```
class Post(models.Model):
   title = models.CharField(max_length=255)
   author = models.CharField(max_length=50, blank=True, null=True)
   preview = models.TextField()
   text_content = models.TextField(blank=False, null=False)
   image = models.ImageField(blank=True, null=True)
   date_added = models.DateTimeField(auto_now_add=True)
   source_link = models.CharField(max_length=254, blank=True, null=True)
```

Comment Model:
Holds data for blog post comments
```
class Comment(models.Model):
   post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
   name = models.CharField(max_length=254)
   email = models.EmailField()
   body = models.TextField()
   date_added = models.DateTimeField(auto_now_add=True)
```

#### Checkout app -
Handles payment functionality and all checkout pages.

```
Order Model:
Holds data of user who created the order, the items in the users shopping bag at the time of order, the order cost and unique stripe payment id.
class Order(models.Model):
   order_number = models.CharField(max_length=32, null=False, editable=False)
   user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                    null=True, blank=True, related_name='orders')
   full_name = models.CharField(max_length=50, null=False, blank=False)
   email = models.EmailField(max_length=254, null=False, blank=False)
   phone_number = models.CharField(max_length=20, null=False, blank=False)
   country = CountryField(blank_label='Country *', null=False, blank=False)
   postcode = models.CharField(max_length=20, null=True, blank=True)
   town_or_city = models.CharField(max_length=40, null=False, blank=False)
   street_address1 = models.CharField(max_length=80, null=False, blank=False)
   street_address2 = models.CharField(max_length=80, null=True, blank=True)
   county = models.CharField(max_length=80, null=True, blank=True)
   date = models.DateTimeField(auto_now_add=True)
   delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
   order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
   grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
   original_bag = models.TextField(null=False, blank=False, default='')
   stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
```

```
OrderLineItem Model:
Holds data on which specific items the user ordered.
order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
   product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
   product_size = models.CharField(max_length=2, null=True, blank=True) # XS, S, M, L, XL
   quantity = models.IntegerField(null=False, blank=False, default=0)
   lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
```

#### Contact app -
Displays the contact page


#### Products app -
Handles product pages and all product informations.

```
Category Model:
Holds product category names
   name = models.CharField(max_length=200)
   friendly_name = models.CharField(max_length=200, null=True, blank=True)
```

```
Product Model:
Holds product details
category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
   sku = models.CharField(max_length=200, null=True, blank=True)
   name = models.CharField(max_length=200)
   description = models.TextField()
   has_sizes = models.BooleanField(default=False, null=True, blank=True)
   price = models.DecimalField(max_digits=6, decimal_places=2)
   image_url = models.URLField(max_length=1024, null=True, blank=True)
   image = models.ImageField(null=True, blank=True)
```

```
ProductReview Model:
Holds product review content and user who left the review.
class ProductReview(models.Model):
   product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
   user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
   content = models.TextField(blank=True, null=True)
   stars = models.IntegerField()
   date_added = models.DateTimeField(auto_now_add=True)
```

#### Profiles app -
Handles user profile pages and information.

```
UserProfile Model:
Holds logged in users information.
user = models.OneToOneField(User, on_delete=models.CASCADE)
   default_phone_number = models.CharField(max_length=20, null=True, blank=True)
   default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
   default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
   default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
   default_county = models.CharField(max_length=80, null=True, blank=True)
   default_postcode = models.CharField(max_length=20, null=True, blank=True)
   default_country = CountryField(blank_label='Country', null=True, blank=True)
```

#### Support app
Displays the support page


### Relationship

Below is a diagram showcasing the relationships between the models.

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1621286435/ms4/my_project_visualized_ekzd2k.png)

-----

## Existing Features

### Off Canvas Nav Bar

This feature is normally reserved for mobile viewports on sites but since so many people browse the web on mobile devices these days, there is more of a trend of using the off canvas menu on desktop viewports. Hence it was chosen for this project as it also keeps the minimalistic feeling of the site and garners a feeling of similarity when looking at the site through a desktop viewport or a mobile viewport.

### Delivery Heading

This header can be found throughout the site and is a constant reminder of the great value when shopping through the site that deliveries are always free. Most competitors always charge and so it was important to really showcase this competitive advantage.

### Shop By Product

This call to action on the home page invites the user to look through the available categories. 

### Profile Icon on nav header

This icon changes depending on the signed in status of the user. If the user is signed in, the same icon is displayed but with a small tick to indicate the signed in status. The icon also takes the signed in user to their profile if they are signed in or to the sign in page if they are not.

### Search

Search functionality is an important factor of the site since the users will most likely be searching for the product names as these will be pushed in marketing by the site owners. These names are searchable in the actual product names or descriptions.

### Basket Icon with dynamically updating item quantity

The basket icon is displayed initially as an empty basket, once a user adds a product to their bag, the basket icon will then show the number of products in the bag at the moment. This number changes dynamically to always reflect the amount of items in the bag.

### Blog

The blog is an important part of the site to also give more value to users of the site and encourage them to continue to visit even if they dont buy anything.

### Blog comments

Comments on blog post allow for interaction between site users and post authors, it is an easy way to increase the small boutique feeling of the site and company and make users feel good about the site owners being accessible.

### Add/delete/edit blog posts

The ability to add, delete and edit blog posts is important to allow for the continual addition and maintenance of the blog section of the site.

### Add/delete/edit products

The ability of to add, delete and edit products is also of the utmost importance to allow the site owners to have flexibility in their offerings, adjust when necessary & keep things fresh on the site.

### Organise products by category

The site only has 4 category choices and so the option to filter by category is actually the main sorting/filtering choice. The total amount of products on the site is not high so users will use the shop by category or menu category choice as the main sorting function.

### User Profiles

User profiles allow the site users to save their personal information into a profile for the next time they purchase something on the site. It also allows them to find their previous order information for reference.

### Special offers/exclusive category

This category will be for recycled or one of a kind pieces produced by the site owners. It was important to be able to differentiate between continued products and one time only exclusive products. 

### Care & Size guide

The size and care guides found on the product detail page allows the site user to get relevant information at the right point in the purchase journey, when they are choosing a size and deciding whether to put the product in their bag. They get all the information they need to make an informed decision.

### FAQ section

The FAQ section gives users answers to common questions so that they dont have to go through the hassle of contacting the site owners and also encourages a feeling of clarity of information again allowing for informed decisions about products and the purchase journey.

### Secure payments with stripe

The payments on the site are handled securely by stripe. By using stripe, the site’s payment information is handled in a very secure way and one which they might already be familiar with since stripe is used for many ecommerce site’s payment solutions.

### Email order confirmation

The email confirmation gives site users another piece of information to refer to about their order/purchase. It is an important part of the ecommerce purchase journey and an expectation that users receive some sort of order confirmation to be able to be satisfied that the order they made has actually been received and confirmed.


### Pagination

Pagination on the products page allows for site users to jump through different pages instead of having to scroll through all the products which may not be easy/efficient for all users.

-----

## Features Left To Implement

### Personalised profile page with picture
A user being able to further personalise their profile page with a profile picture is a feature that can give more of a “member” feeling however since the profile page would be for the time being the only place the picture would be displayed, it was decided that this feature could potentially be added at a later date

### Like/wishlist functionality
This feature is often found on larger product base ecommerce sites, however the small boutique like concept of the store meant that the benefits of having this feature would not be as much. This is still a much wanted feature from the site owners but something that just did not have priority in time to build.

### Filtering for new/best sellers/most viewed products + Product sorting ascending/descending/by price
As mentioned above, the store will not have many products available so these features were pushed to the back of the list. A good to have feature but not as necessary as others for this particular site.


### Multiple images of product on product detail page
This was a much wanted feature but one there was not enough time to implement. A second or third product image for users to look at on the product detail page would really increase the chances of a purchase or allow users to be more informed when deciding whether to make a purchase or not.

### Generate links to similar items on product detail, bag, checkout and other pages
This is another feature that is very common on other ecommerce sites, users being shown links to products that are similar to the ones they are currently looking at or have looked at. It didnt have so much of a priority since the site owners believed it could detract from the boutique small business feeling of the site. It is a feature that could be implemented though as the site and business grows.

### Click to copy url share icon:
This was a feature that would not have really solved a need or question since you can just copy a url in the address bar but it would have made it more convenient to just press a link and have the url copied automatically . This nature of the feature meant that it was deemed not a priority and time was given to other higher priority features.

### Add product customisation notes to order line items
The ability to add notes to products for customisation is a feature that the site owners believe they will need at some point in the future as their customer base grows but they want to push their core offerings as what they are for the time being.

### Contact customers that have profiles
Being able to contact customers that have created profiles would allow the site owners to market relevant products, discounts and other information to site users. This is again something they want functionality for in the future but for now they want the brand to expand more organically and want to make use of this feature when they have more of a customer base.

### Custom 404 & 500 error page
This feature would give users a more professional and well defined message which would reflect the site and brand better. Time and priority to other features is why this was not implemented.

### Defensive Programming
By implementing more defensive programming throughout the site, it would be protected from more security threats and errors which gives a smoother experience to the users and site owners. Time and priority to other features is why this was not implemented.

### Reverse back to previous page on login
If accessing login page from anywhere but home page, the site user would be redirected back to that page on eventual sign in. Time and priority to other features is why this was not implemented.

-----

## Technologies Used

#### Front End
- Bootstrap 5 inc. packaged javascript & Icons. - used for layout and various components.
- jQuery - Used for bootstrap toasts & various other front-end interactive elements.
- Mmenu.js, mhead.js & mburger.js - Off canvas nav with animated icon & pull down anytime header.
- TinyMCE - WYSIWYG rich text editor.
#### Back-End
- Django - Main project framework
- Python - Main backend language
- Pip3 - Python package installer
- SQLite - database used in development
- PostgreSQL - database used in deployment
- Stripe - used for handling payments
- AWS S3 - Used for storage of static and media files for deployed site.

#### Global
- Gitpod - IDE used for project
- Git - Version control 
- Github - Hosting of project files
- Heroku - Used for project deployment
- Figma - Used for creating wireframes
- Compressjpeg.com - Used for reducing image file size.
- Coolors.co - used for generating colour palettes.

-----

## Testing

Testing documentation can be found [HERE](ms4_testing.md)

-----

## Deployment

### My Set Up
My IDE of choice for this project was GitPod. I used the [Code Institute template](https://github.com/louparker/gitpod-full-template), by clicking on the green "use this template" link.

After being directed to the create new repository from template page, I typed in the project name and clicked the create repository from template button. I then clicked on the GitPod button which was on the newly created repository page I was directed to. This created a GitPod workspace based on the repository.

The project is being hosted live on heroku with AWS S3 hosting the static and media files. Git was used for version control while GitHub was used to host the project repository.


### Run Project Locally

In order to get the project up and running on your local machine, follow these steps.

#### Requirements:
- Python3
- Pip
- Git
- IDE of your choice
- A Stripe account


#### Step One, clone repository into local environment:

- Click this link to open the main repository page: [HERE](https://github.com/louparker/myochlinn).
- Click the code button
- Copy the link you are given to your clipboard
- On your IDE of choice, open terminal and navigate to whichever directory you want the repository cloned to. Once in the desired directory, type `git clone`, then paste the URL copied from the Github repository. The command should look something like this:

`git clone https://github.com/louparker/myochlinn.git`

- Press enter & you should have a local cloned version of the repository.



#### Step 2, Install requirements:
- While you are still in the terminal, type `pip3 install -r requirements.txt`, this will install all the required softwares to run the project.
- You now need to set up the database with environment variables. Create a file titled `env.py` and make sure it is placed in the of this file structure, on the same level as the `app.py` file. Open the file and type the following lines:


```
 os.environ.setdefault('SECRET_KEY', '<your_variable_here>')
 os.environ.setdefault('DEVELOPMENT', 'True')
 os.environ.setdefault('STRIPE_PUBLIC_KEY', '<your_variable_here>')
 os.environ.setdefault('STRIPE_SECRET_KEY', '<your_variable_here>')
 os.environ.setdefault('STRIPE_WH_SECRET_CH', '<your_variable_here>')
 os.environ.setdefault('STRIPE_WH_SECRET_SUB', '<your_variable_here>')
```

- The `SECRET_KEY` is a value key of your own choice but it is recommended to be as secure as possible so it is recommended to use the Django secret key generator. `DEVELOPMENT` is true when the setup is local whereas it would be false if it was a remote setup with data being imported from outside the setup.
 
- All `STRIPE` variables are taken from the stripe website and are needed to set up proper functioning payments and orders.
- Once that is all set up, you are now ready to run the app. In the terminal, type python3 (depending on python version) manage.py runserver , this will run the python file and depending on your IDE should open a port and give you a link to access it through either an in-window preview or your browser.

### Heroku Deployment

#### Requirements:
- Heroku account
- [AWS S3 Account set up](https://aws.amazon.com/s3/getting-started/)

In order to host static files and images with AWS, you will need to create an AWS account. Additionally, you have to create:

- An AWS S3 Bucket
- A Bucket Policy
- A Group
- An Access Policy
- A User

Links to help
[HERE](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)
[HERE](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)

- Go to heroku.com & sign in or create a user if you haven't got one already.
- Press the new button & click create a new app.
- Choose your app name and region (closest to where you live).
- At this stage you will want to set up the heroku app with the github repository. Click on the deploy tab and choose connect to github.
- From the search input that opens, search for your repository by name and click the search button.

- Once the desired repo has been found, press the connect button.
- You will then need to set the environment variables since the env.py file is not pushed to github. To do this, open the settings menu and click on the reveal config vars button.

- Go to the resources tab and search for Heroku Postgres. Choose the “hobby dev - free” option and submit the order form.
- On the settings.py file, you will need to comment out the 'SQLite and Postgres databases' section and UNcomment the 'PostgreSQL Database' section. (this is temporary, nothing should be pushed/committed just yet). 
- Add the database URL from Heroku & migrate your models to the PostgreSQL database with:
 python3 manage.py migrate
- You will then need to create a superuser which will be the credentials you use to log in to the admin page and manage the database. Type this in the terminal:

 `python3 manage.py createsuperuser`

- Fill in a username, password and email as required.
- Back in the settings.py file, you can now delete the 'PostgreSQL Database' section and uncomment the 'SQLite and PostgreSQL Databases' section. This means that either database can now be used interchangeably.
- Update the requirements.txt file to ensure a clean deployment with:

 `pip3 freeze --local > requirements.txt`

- Create a Procfile by inputting the following into the terminal:

 `web: gunicorn <your_application_here>.wsgi:application`

- You can now commit your changes and push to GitHub.
- Copy the variables from the env.py file one by one into the heroku config vars. They would be:
```
key: 'SECRET_KEY', value: “your_variable_here”
key: 'DEVELOPMENT', value: "True"
key: 'STRIPE_PUBLIC_KEY', value: "your_variable_here"
key: 'STRIPE_SECRET_KEY', value: "your_variable_here"
key: 'STRIPE_WH_SECRET_CH', value: "your_variable_here"
key: 'STRIPE_WH_SECRET_SUB', value: "your_variable_here"
```

- Make sure the values are exactly the same as the ones you have in the env.py file.
- You will also need some extra variables that you would need to properly connect to aws S3, these would be:
```
key: AWS_ACCESS_KEY_ID, value: "AWS access key ID"
key: AWS_SECRET_ACCESS_KEY, value: "AWS secret access key"
key: USE_AWS, value: "True"
```

- At this stage you are ready to enable automatic deployment. You will want to push any changes you have made to github for convenience sake before you do this.
- Click on the deploy tab.
- Go down to the automatic deploy section & select the branch you intend to deploy. 
- click enable automatic deploys. This means github is talking to heroku and whatever you push to github will be in your deployed heroku app.
- If there were any errors with the deployment, double check you have your Procfile and requirements file, if the requirements file is not there, you can type in your terminal pip3 freeze > requirements.txt. This will also make sure you have the most recent requirements pushed to GitHub & Heroku. If the Procfile is missing, you can type `echo "web: python3 app.py" > Procfile` (with a capital P).
- You can now use the site admin to add products and blog posts to the site and the content media will be pushed to AWS for storage.

### Forking

This is how you can "fork" the project without affecting the main branch. Which means you can change & edit it as a repository on your own GitHub profile.

1. Log in to GitHub.
2. Click on the following link to be taken to this repository's main page: [HERE](https://github.com/louparker/myochlinn).
3. To the right of the repository name, you will see a "fork" button, click it.
4. You will now have a copy of this repository on your own GitHub account.
5. When you are done editing to your hearts content, you can click the "new pull request" button which allows the repository owner (me!) to include your work in the original project.

-----

## Credits

### Content
All design, content and code (unless specified below) were created by myself.

Specified code usage includes:
- [Django Documentation](https://docs.djangoproject.com/en/3.2/)
- [Python3 Documentation](https://docs.python.org/3/contents.html)
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [mmenu.js](https://mmenujs.com/)
- Code Institute Course Content
- [Animations from hover.css](https://ianlunn.github.io/Hover/)
- [Blog code from "Code with Stein"](https://codewithstein.com/build-a-simple-blog-using-django-3-in-under-20-minutes/)
- [Stripe Documentation](https://stripe.com/docs)
- [Checkout loading animation from Luke Haas](https://projects.lukehaas.me/css-loaders/)


The following sites were used for beautifying, optimizing images and adding correct vendor prefixes to my code:
- [Autoprefixer CSS](https://autoprefixer.github.io/)
- [Code Beautify](https://codebeautify.org/)
- [TinyPNG](https://tinypng.com/)
- [CompressJPEG](https://compressjpeg.com/)

All product and homepage images from:
[MonicaVinader.com](https://www.monicavinader.com/)

All blog images from:
[simonewalsh.com](https://simonewalsh.com/)

All other images from Unsplash


### Acknowledgements

- Stack Overflow as always was a massive help.
- Special thanks to my mentor Maranatha for regular words of wisdom and helping guide me to the right conclusions.
