# Testing

### Table Of Contents
1. [Code Validation](#code-validation)
2. [Browser Compatibility](#browser-compatibility)
3. [Manual Testing](#manual-testing)
5. [User Story Testing](#user-story-testing)
6. [User Testing](#user-testing)
7. [Bugs & Issues](#Bugs)

-----

### Code Validation

#### W3C HTML Validator:

- About app templates:
Pass (only errors due to template formatting)

- Bag app templates:
One error:
In the bag.html there are some id’s that are the same where they should be unique by best practice. This is due to the reuse of code during the mobile version re-factoring. What could be done to properly fix this error is to create separate html files which would take in the html code for these repeated sections so that they can be included where necessary.

- Blog app templates:
Pass (only errors due to template formatting)

- Checkout app templates:
Pass (only errors due to template formatting)

- Contact app templates:
Pass (only errors due to template formatting)

- Products app templates:
Pass (only errors due to template formatting)

- Profiles app templates:
Pass (only errors due to template formatting)

- Support app templates:
Pass (only errors due to template formatting)

- Home app templates:
Pass (only errors due to template formatting)

- Base.html:
Pass (only errors due to template formatting)

- Allauth & other external app html templates:
Not tested due to heavily tested nature of these applications before release.



#### Jigsaw CSS Validator
- styles.css :
Pass with no errors but warnings for unknown webkit vendor extensions.

- checkout.css :
Pass with no errors but warnings for unknown webkit vendor extensions.

- profiles.css :
Pass with no errors and no warnings.

#### Javascript Validator (JSHint):

Javascript was re-used throughout different apps so to avoid retesting, the js testing is for all apps is grouped into this section.

#### All apps js:
No major errors
Stripe_elements section on checkout.html had 2 issues which I made a note of as I did not want to cause any issues with it for the time being since the functionality is working just fine.

#### Uncaught SyntaxError: Unexpected token 'export':
This is coming from the mburger.js file which is an external file. I chose not to explore this error in the interest of time and due to the fact that the plug-in is working fine as it is. Time can be spent at a later date to investigate this error.



#### PEP8 Validator:

- Common to see flake8(e501 line too long), these errors are difficult to fix consistently as they require solutions that arent always effective or efficient. I have therefore chosen to ignore them where there is not much that can be done about them and where they can be fixed, they have been.

-----

### Browser Compatibility

Browser compatibility was checked using [BrowserStack](https://www.browserstack.com/live). I went through compatibility testing on a Chrome v90, Firefox v88, Safari 5.1 + 14, Edge v90. Details included in the table below.

|Criterea             |Galaxy S21 Ultra|Moto G4   |Galaxy S5 |Pixel 2   |Pixel 2 XL|iPhone SE |iPhone X|iPhone 11|iPhone 12  |iPad      |iPad Pro  |Surface Duo|Galaxy Fold|Laptop (+1024px)|Laptop (+1440px)|
|---------------------|-----------|----------|----------|----------|----------|----------|------------|-----------------|----------|----------|----------|-----------|-----------|----------------|----------------|
|Renders As Expected? |PASS       |PASS      |PASS      |PASS      |PASS      |PASS      |PASS        |PASS             |PASS      |PASS      |PASS      |PASS       |PASS       |PASS            |PASS            |

Testing was also done on a real life Iphone 11, a Samsung Galaxy S21 Ultra, an Ipad and a Macbook pro. The search icon displays with a strange border and bevel but everything works fine apart from that. The font on samsung & all android devices it seems did not want to update correctly when using a custom font. At this point the font was changed to a default one for continued and consistent ux and ui. This does not seem to have fixed the issue but it will continue to be investigated.

-----

|Criteria              |Chrome v90     |Firefox v88    |Safari v14  |Edge v90       |
|----------------------|:-------------:|:-------------:|:--------------:|:-------------:|
|Renders As Expected?  |PASS           |PASS           |PASS            |PASS           |

-----


### Manual Testing

Manual testing for functionality and features was done on each page and for each feature. Each test is answered yes or no, the no's will be investigated/explained.

| Page               | Test Number | Test                                                                                                                             | Pass/Fail |
|--------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------|-----------|
| Home/index/base    | 1           | Can I see all images                                                                                                             | P         |
| Home/index/base    | 2           | Am I redirected to the correct product category if I click something on the shop by category section                             | P         |
| Home/index/base    | 3           | Does the off canvas menu display properly when clicked                                                                           | P         |
| Home/index/base    | 4           | Is the profile icon correct for if i am logged in or not                                                                         | P         |
| Home/index/base    | 5           | Does the search functionality work                                                                                               | P         |
| Home/index/base    | 6           | Does the basket icon show the correct quantity and take me to the basket page when clicked                                       | P         |
| Home/index/base    | 7           | Does the “My & Linn” logo take me to the homepage                                                                                | P         |
| Home/index/base    | 8           | Do all the footer icons & links work                                                                                             | P         |
| Products           | 1           | Can I scroll through pages of products                                                                                           | P         |
| Products           | 2           | Do the links to the respective product detail page work                                                                          | P         |
| Products           | 3           | If I am a superuser/admin, do the delete/edit links work                                                                         | P         |
| Products           | 4           | Is the page responsive and all content visible                                                                                   | P         |
| Products           | 5           | Do all nav & footer links and the off canvas nav menu work on this page                                                          | P         |
| Product Detail     | 1           | If I am a superuser/admin, do the delete/edit links work                                                                         | P         |
| Product Detail     | 2           | Can i easily choose size and colour of the product                                                                               | P         |
| Product Detail     | 3           | Can I see a size guide for the product                                                                                           | P         |
| Product Detail     | 4           | Can I see a care guide for the product                                                                                           | P         |
| Product Detail     | 5           | Is the page responsive and all content visible                                                                                   | P         |
| Product Detail     | 6           | Do all nav & footer links and the off canvas nav menu work on this page                                                          | P         |
| Shopping bag       | 1           | Can I see clearly all the items in my shopping bag                                                                               | P         |
| Shopping bag       | 2           | Can i change the amount or delete the items in my bag                                                                            | P         |
| Shopping bag       | 3           | The continue shopping and checkout links both work                                                                               | P         |
| Shopping bag       | 4           | Is the page responsive and all content visible                                                                                   | P         |
| Shopping bag       | 5           | Do all nav & footer links and the off canvas nav menu work on this page                                                          | P         |
| Checkout           | 1           | The form is pre-filled if i am signed in                                                                                         | P         |
| Checkout           | 2           | I can see the total amount that I need to pay                                                                                    | P         |
| Checkout           | 3           | The form looks professional and safe                                                                                             | P         |
| Checkout           | 4           | Is the page responsive and all content visible                                                                                   | P         |
| Checkout           | 5           | Do all nav & footer links and the off canvas nav menu work on this page                                                          | P         |
| Checkout           | 6           | Do validation errors show when trying to submit the form without filling out all the required information in the correct format. | P         |
| Order confirmation | 1           | Link to blog works                                                                                                               | P         |
| Order confirmation | 2           | Can see clearly the order confirmation                                                                                           | P         |
| Order confirmation | 3           | Received an email confirmation of the order                                                                                      | P         |
| Order confirmation | 4           | Is the page responsive and all content visible                                                                                   | P         |
| Order confirmation | 5           | Do all nav & footer links and the off canvas nav menu work on this page                                                          | P         |
| About us           | 1           | Information about site owners displays clearly                                                                                   | P         |
| About us           | 2           | Is the page responsive and all content visible                                                                                   | P         |
| About us           | 3           | Do all nav & footer links and the off canvas nav menu work on this page                                                          | P         |
| Contact Us         | 4           | Information on how to contact site owners displays clearly                                                                       | P         |
| Contact Us         | 5           | Is the page responsive and all content visible                                                                                   | P         |
| Contact Us         | 6           | Do all nav & footer links and the off canvas nav menu work on this page                                                          | P         |
| Support/FAQ        | 1           | Faq and delivery/returns information  displays clearly                                                                           | P         |
| Support/FAQ        | 2           | Is the page responsive and all content visible                                                                                   | P         |
| Support/FAQ        | 3           | Do all nav & footer links and the off canvas nav menu work on this page                                                          | P         |
| Product Management | 1           | Can fill in form to add a new product                                                                                            | P         |
| Product Management | 2           | The new product is added and you are redirected to the new products product detail page                                          | P         |
| Product Management | 3           | I get a message confirming that the new product has been added.                                                                  | P         |
| Product Management | 4           | I can successfully upload an image for the new product.                                                                          | P         |
| Product Management | 5           | Is the page responsive and all content visible                                                                                   | P         |
| Product Management | 6           | Do all nav & footer links and the off canvas nav menu work on this page                                                          | P         |
| Product Management | 7           | Do validation errors show when trying to submit the form without filling out all the required information in the correct format. | P         |
| Blog               | 1           | User can see all currently available posts                                                                                       | P         |
| Blog               | 2           | Super user can edit and delete posts                                                                                             | P         |
| Blog               | 3           | Clicking the post image takes me to the respective post detail page                                                              | P         |
| Blog               | 4           | Is the page responsive and all content visible                                                                                   | P         |
| Blog               | 5           | Do all nav & footer links and the off canvas nav menu work on this page                                                          | P         |
| Blog Management    | 1           | Can fill in form to add a new blog post                                                                                          | P         |
| Blog Management    | 2           | The new blog post is added and you are redirected to the post detail page                                                        | P         |
| Blog Management    | 3           | I get a message confirming that the new post has been added.                                                                     | P         |
| Blog Management    | 4           | I can successfully upload an image for the new post.                                                                             | P         |
| Blog Management    | 5           | Is the page responsive and all content visible                                                                                   | P         |
| Blog Management    | 6           | Do all nav & footer links and the off canvas nav menu work on this page                                                          | P         |
| Blog Management    | 7           | Do validation errors show when trying to submit the form without filling out all the required information in the correct format. | P         |
| Profile/My Account | 1           | I can see my default delivery information (if saved from checkout or previously updated)                                         | P         |
| Profile/My Account | 2           | I can update my delivery information.                                                                                            | P         |
| Profile/My Account | 3           | I can see all my previous order history.                                                                                         | P         |
| Profile/My Account | 4           | The link to view specific orders works.                                                                                          | P         |
| Profile/My Account | 5           | Is the page responsive and all content visible                                                                                   | P         |
| Profile/My Account | 6           | Do all nav & footer links and the off canvas nav menu work on this page                                                          | P         |
| Profile/My Account | 7           | Do validation errors show when trying to submit the form without filling out all the required information in the correct format. | P         |
| Sign-in/out        | 1           | Sign in / out links work                                                                                                         | P         |
| Sign-in/out        | 2           | Cancel link for sign out works.                                                                                                  | P         |
| Sign-in/out        | 3           | I get a message when signing in /out.                                                                                            | P         |
| Sign-in/out        | 4           | I am redirected to the password reset page when clicking the forgot password link.                                               | P         |
| Sign-in/out        | 5           | I can click sign up and be redirected to the sign up page.                                                                       | P         |
| Sign-in/out        | 6           | Is the page responsive and all content visible                                                                                   | P         |
| Sign-in/out        | 7           | Do all nav & footer links and the off canvas nav menu work on this page                                                          | P         |
| Sign Up/Register   | 1           | I can successfully create a user.                                                                                                | P         |
| Sign Up/Register   | 2           | I can click the sign in link to be redirected to the sign in page.                                                               | P         |
| Sign Up/Register   | 3           | Do validation errors show when trying to submit form without filling out all the required information in the correct format.     | P         |
| Sign Up/Register   | 4           | Is the page responsive and all content visible                                                                                   | P         |
| Sign Up/Register   | 5           | Do all nav & footer links and the off canvas nav menu work on this page                                                          | P         |
|                    |             |                                                                                                                                  |           |

-----


### User Story Testing

| User Story Number | As A/An      | I should be able to...                                                         | So that I can ...                                                                                                    | Can I do this? Are the aims met? |
|-------------------|--------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 1                 | Site Owner   | Add products                                                                   | Have new Items available for purchase on the site.                                                                   | Y                                |
| 2                 | Site Owner   | Delete products                                                                | Have correct available stock information on the site.                                                                | Y                                |
| 3                 | Site Owner   | Edit products                                                                  | Change & update relevant stock information.                                                                          | Y                                |
| 4                 | Site Owner   | Add, modify & delete blog posts                                                | Keep the blog section of the site fresh                                                                              | Y                                |
| 5                 | Site Owner   | View a blog on the site with relevant tips, advice and interesting content     | Add value to the website and brand as a whole                                                                        | Y                                |
| 6                 | Site Owner   | Understand the purpose of the site                                             | Decide whether I want to invest my time into it.                                                                     | Y                                |
| 7                 | Site Owner   | Site to be readable on all screen sizes.                                       | Shop on the site no matter which device I am using.                                                                  | Y                                |
| 8                 | Site Visitor | View all available products                                                    | See which potential products I can purchase                                                                          | Y                                |
| 9                 | Site Visitor | View a specific category of products                                           | Find a specific type of jewelry without having the inconvenience of seeing other categories I know I do not want     | Y                                |
| 10                | Site Visitor | See individual product details                                                 | Learn more about the specific product                                                                                | Y                                |
| 11                | Site Visitor | Easily see special offers/exclusive items                                      | Take advantage of temporary offers and products                                                                      | Y                                |
| 12                | Site Visitor | See total shopping bag information at any time                                 | Control how much I am spending                                                                                       | Y                                |
| 13                | Site Visitor | Search for product by words in name or description                             | Find a specific product                                                                                              | Y                                |
| 14                | Site Visitor | See on search results, what I searched for and number of results found         | Reference the specific word I searched for and see how many items are matching the search                            | Y                                |
| 15                | Site Visitor | View items in basket with short description of each                            | See which products I am thinking about purchasing and be reminded of why I want to purchase them                     | Y                                |
| 16                | Site Visitor | Delete or change quantity of items in basket                                   | Easily change my mind or add/remove quantities of the same product without having to go to the specific product page | Y                                |
| 17                | Site Visitor | Easily see and choose size/colour/quantity to purchase                         | Purchase with the specification I am comfortable with                                                                | Y                                |
| 18                | Site Visitor | View information on how to care for product on product page                    | Keep the product in good condition for a long time                                                                   | Y                                |
| 19                | Site Visitor | View a size guide for relevant products                                        | Feel sure about which size is best for me                                                                            | Y                                |
| 20                | Site Visitor | Learn more about the business & their values from the about page               | Feel more comfortable buying from the company                                                                        | Y                                |
| 21                | Site Visitor | Have easy access to a contact page                                             | Have an easy way to contact the company should I have any feedback or comments to make.                              | Y                                |
| 22                | Site Visitor | Easily find out delivery information                                           | Easily see how long it will take to receive my product                                                               | Y                                |
| 24                | Site Visitor | Find an FAQ section                                                            | Quickly find answers to common questions.                                                                            | Y                                |
| 25                | Customer     | Easily enter my payment details                                                | Have a smooth payment experience                                                                                     | Y                                |
| 26                | Customer     | See & feel that the payment process is secure                                  | Feel comfortable putting my payment information on the site                                                          | Y                                |
| 27                | Customer     | See an order confirmation after payment process is complete                    | Be sure that the order has gone through                                                                              | Y                                |
| 28                | Customer     | Receive email confirmation of order after website checkout process is complete | Have my own copy of an order confirmation and can relay back to this for relevant information.                       | Y                                |
| 29                | Customer     | Easily be able to register an account                                          | Take advantage of benefits of having an account on the site                                                          | Y                                |
| 30                | Customer     | Receive email confirmation of my account registration                          | Be sure that the registration process has gone through                                                               | Y                                |
| 31                | Customer     | Easy access to the log in/out functionality at all times                       | Easily log in or out of my account at any point when on the website.                                                 | Y                                |
| 32                | Customer     | Recover my password in case i forget                                           | Easily create now password and continue to shop on website                                                           | Y                                |

-----

### User Testing

While testing the site with family and friends, feedback was taken on how to improve the user experience and thoughts on features. The feedback was generally good and positive but there were also opportunities for improvement.

The following suggestions were made:

Change home page main image(hero image) as the picture looked like someone in chains. 
(Image was changed)
Add comments functionality to the blog posts.
(Commenting functionality was added)
Change the look of the footer, there is too much space on one side.
(previous footer look had all link items in one column to the left in all viewports, this has been changed to the current look where link items are spread to take up the space evenly)
I cant see the menu link labels or read them so well, the font is nice but really narrow.
(The menu link labels were made pure white in colour and the text was spaced out more and increased in font size to improve readability)
I dont want to see my bag contents everytime i get a message notification on the site.
(The messages that do not concern the shopping bag have been adjusted to not include the shopping bag information.)


### Bugs & Issues

#### Plus and minus buttons on bag.html - Status - FIXED
The plus and minus buttons on this page would position incorrectly when changing to a mobile viewport (between 340px & 380px), to fix this, the bag.html structure was refactored to better show on mobile viewports.

#### Form Labels - Status - ONGOING
Since using crispy forms, I was confused as to how to get form labels to show, a lot of research eventually ended up with a simple fix, however the form labels as they are, are not very user friendly. A future change would be to find out how to give a specific name to each label that would be more user friendly.

#### Unexpected token ’export’ on mburger.js - Status - ONGOING
This is an issue with the external mburger.js plug-in that i am using for the off canvas menu. In the interests of time and since it is not breaking functionality, this issue will be investigated at a later date.

#### Product results not showing total items - Status - ONGOING
Due to the pagination functionality, the quantity in the ‘we found x products’ text is incorrect. It is only correct for the amount of items on that specific page but does not reflect the total amount of items within the current category. This is another bug that will be fixed at a later date in the interest of time and prioritising other issues.

#### Font not correct on certain mobile devices - Status - ONGOING
In my testing on android devices, the ‘Emberly Medium’ font seems to be not working as intended. Research into why this was happening lead me to include various different src font files in the css and static files directory. Choosing to change font into a default font (Lucida Sans) seems to have also not fixed the issue, investigations will continue to understand what is causing this issue as it is a priority 

#### The ‘X’ close icon on the off canvas menu does not do anything - Status - ONGOING
The ‘x’ in the off canvas menu really should be a clickable link to close the menu, however I could not seem to get it to function in that way. The overall functionality is that a click anywhere outside the menu or a click of a menu item will automatically close it. However this removes the need for the ‘x’. For the time being I will not investigate more how to make the ‘x’ function properly or figure out how to remove it. It will be an issue to investigate further at a later date.

#### JS not loading properly - Status - ONGOING
Halfway through development of the project, I started having issues with javascript and the location in the base.html of the script tags. It seemed that if they were at the top, static js files would not be found when trying to include them in templates. After many hours trying to find a solution, a workaround of including the raw js directly in the respective templates was used. This might not be best practice but it was a necessary evil in order to move on from an issue that I spent too long on.

#### TinyMCE outputting html tags with text - Status - FIXED
This was an issue with the TinyMCE WYSIWYG rich text editor plug in. If i uploaded a new blog post, it would function just fine but the actual post would show the inputted text within `<p>` tags and `<br>` tags where a new line was started. After a few hours of looking for a fix and trying to figure out the right syntax within this project, I figured out that the content being loaded on the html template needed to have a ‘safe’ attribute. This removed all unwanted html code from the output and made the functionality work 100%.

#### Google social auth login - Status - ONGOING
I wanted to implement social auth via the gmail api but could not get it to function in the right way. I got as far as selecting which email to log in with and then got stuck on a page not found error. I managed to figure out that the issue came from google not redirecting to the correct URL since if I manually adjusted the URL to include the correct host, the log in worked just fine. But I did not have the time to spend figuring out how to get the api to redirect to this correct URL. For this reason this feature has been removed for the moment but will be investigated as a priority.

