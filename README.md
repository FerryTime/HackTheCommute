# HackTheCommute: Ferry Time

The purpose of this app is to help ferry commuters in Washington State.

This application was developed on 2015-03-2[0-2] for the 2015 Seattle [Hack The Commute](http://hackthecommute.seattle.gov).

![We like Fairies and Ferries!](https://github.com/FerryTime/HackTheCommute/blob/master/ferrytime/Ferry_Wenatchee_enroute_to_Bainbridge_Island_WA.jpg)


Our app is live at http://fairytime.herokuapp.com/.

Screen Shots:

![Screen1](https://github.com/FerryTime/HackTheCommute/blob/master/Screenshot_2015-03-22-16-26-26.png)

![Screen2](https://github.com/FerryTime/HackTheCommute/blob/master/Screenshot_2015-03-22-16-27-25-1.png)

## Challenge and Approach

Our submission is for [Challenge #2: Improve the commuter experience in any single mode](https://codeforseattle.hackpad.com/Submission-Guidelines-UTxrlISdazl).

Our approach for satisfying this challenge was to:

1.  Our Concept.
    - Commuting via ferry can be troublesome at best
        - Example from the [King5 News](http://www.king5.com/story/news/local/seattle/2014/08/19/ferry-passengers-frustrated-over-problems/14182429/) about the traffic at Fauntleroy
    - Everyone who has used the ferry has the experience of waiting in the queue, not knowing if you'll make it
    - 23 million users depend on the ferry system 
        Many of the surrounding areas need to get into Seattle, which has the highest income average in the region

2.  Execution.
    - Awesomeness of Ferry Fairy, to be seen in action!

3.  The Impact.
    - People have a better travel experience by knowing what to expect
    - One app to rule them all
    - Commuters can plan and adjust according to realtime data of ferry waits
    - From this app, it can build more real time information for WSF, which can inform policy makers
    - Can collect a large dataset of users and wait times 

4.  Implementation & Sustainability.
    - Need More Routes
        - Currently, only one route
    - Advertising to ferry commuters 
    - Moving forward - need realtime assessment for people "up stream" of the toll booth
      - Utilization of GPS location, User inputted landmarks
      - WSDOT Booth Information
      - Vehicle Detection Loops
    - Connecting with the Ferry Commnunity
    - Parking Space Information for Walk-Ons
    - Sustainability
        - Start with volunteer
        - As usership grows, dataset becomes more valuable

## Team Members

Our team is comprised of:

- [@fierlion](http://github.com/fierlion) - Ray Foote - general dev stuffs
- [@thalijw](http://github.com/thalijw) - Wisam Thalij - general javascript and html stuffs
- [@bkstamm67](http://github.com/bkstamm67) - Brian Stamm - general data stuffs
- [@musickka](http://github.com/musickka) - Katie Musick - general javascript and html stuffs
- [@LathamFell](https://twitter.com/LathamFell) - Latham Fell - general support, father extraordinaire
- [@shawnbuck8](http://github.com/shawnbuck8) - Shawn Buck - general mapping stuffs
- [@qayshp](http://github.com/qayshp) - Qays Poonawala - general dev stuffs

## Technologies, APIs, and Datasets Utilized

We made use of:

- The [WSDOT API Website](http://wsdot.wa.gov/traffic/api/)
    - Specifically, [WSDOT Ferries Terminals] (http://www.wsdot.wa.gov/ferries/api/terminals/rest/help)
    - And, [WSDOT Ferries Schedule] (http://www.wsdot.wa.gov/ferries/api/schedule/rest/help)
- [@wsdot](https://twitter.com/wsdot) WSDOT Twitter feed

## Contributing

In order to build and run our app:

1. Visit our [Heoku hosted mobile web app](http://fairytime.herokuapp.com).

Our code is licensed under the [MIT License](LICENSE.md). Pull requests will be accepted to this repo, pending review and approval.

Copyright (c) 2015 Ferry Time, Incorporated.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
