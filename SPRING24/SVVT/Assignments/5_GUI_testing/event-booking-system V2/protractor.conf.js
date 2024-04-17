/*
 * -----------------------------------------------------------------------
 * File: protractor.conf.js
 * Creation Time: Apr 16th 2024, 8:37 pm
 * Author: Saurabh Zinjad
 * Developer Email: saurabhzinjad@gmail.com
 * Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
 * -----------------------------------------------------------------------
 */

exports.config = {
    directConnect: true, // lets Protractor connect directly to the browser without using a Selenium server
    framework: 'jasmine', // using the Jasmine test framework
    specs: ['e2e/**/*.spec.js'], // specifies where your test files are located
    capabilities: {
        browserName: 'chrome' // specifies which browser to use for testing
    },
    jasmineNodeOpts: {
        defaultTimeoutInterval: 30000 // how long to wait before a test fails
    }
};
