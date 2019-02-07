# -*- coding: utf-8 -*-

import github.tests.Framework as Framework
import github


class AuthYak(Framework.BasicTestCase):
    def testNoAuthentication(self):
        g = github.Github()
        self.assertEqual(g.get_user("YakDriver").name, "Dirk Avery")

    def testOAuthAuthentication(self):
        g = github.Github(self.oauth_token)
        self.assertEqual(g.get_user("YakDriver").name, "Dirk Avery")

    def testUserAgent(self):
        g = github.Github(user_agent="PyGithubTester")
        self.assertEqual(g.get_user("YakDriver").name, "Dirk Avery")

    def testAuthorizationHeaderWithLogin(self):
        # See special case in Framework.fixAuthorizationHeader
        g = github.Github("fake_login", "fake_password")
        with self.assertRaises(github.GithubException):
            g.get_user().name

    def testAuthorizationHeaderWithToken(self):
        # See special case in Framework.fixAuthorizationHeader
        g = github.Github("ZmFrZV9sb2dpbjpmYWtlX3Bhc3N3b3Jk")
        with self.assertRaises(github.GithubException):
            g.get_user().name
