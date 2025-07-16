# 웹 크롤러 테스트용 사이트 목록

다양한 렌더링 방식과 백엔드 프레임워크로 구성된 50개 도메인을 분류한 표입니다. 각 사이트는 HTML 구조와 동적 요소가 달라 크롤러 테스트 시 참고용으로 활용할 수 있습니다.

## 1. Static HTML 기반
- https://example.com - W3C 샘플 정적 HTML
- https://httpbin.org/html - HTML 테스트용 정적 구조
- https://info.cern.ch - 최초의 웹사이트 (완전 정적)
- https://www.gnu.org - 전통적인 HTML 사이트
- https://www.kernel.org - 리눅스 커널 배포 사이트

## 2. PHP 기반 (SSR)
- https://www.php.net - 공식 PHP 문서 사이트
- https://www.wordreference.com - PHP 기반 사전 사이트
- https://www.fmkorea.com - 커뮤니티 사이트 (XpressEngine 기반)
- https://bbs.ruliweb.com - 루리웹, PHP 기반 구조
- https://www.11st.co.kr - 초기엔 JSP+PHP 혼합 구조

## 3. Python(Django, Flask 등) 기반
- https://www.djangoproject.com - Django 공식
- https://docs.python.org - 정적 HTML + Sphinx
- https://realpython.com - Flask + Django 기반 블로그
- https://readthedocs.org - Sphinx 기반 문서
- https://opendart.fss.or.kr - Python 웹 구조 (HTML 복잡)

## 4. Ruby on Rails 기반
- https://rubyonrails.org
- https://www.basecamp.com - RoR 기반 대표 SaaS
- https://dev.to - 커뮤니티 기반 (RoR + SPA 일부)
- https://www.heroku.com
- https://www.shopify.com - RoR 기반 (대규모 SPA 일부 혼합)

## 5. React / Vue 기반 SPA (CSR)
- https://www.notion.so - React 기반 완전 CSR
- https://app.slack.com - React + WebSocket
- https://www.airbnb.com - React 기반 CSR
- https://www.toss.im - Vue 기반 페이지 다수
- https://www.kakaobank.com - Vue + Ajax

## 6. Next.js / Nuxt 등 Hybrid (SSG + CSR)
- https://vercel.com - Next.js 기반
- https://nextjs.org - SSG + ISR 혼합
- https://v3.vuejs.org - Nuxt 기반
- https://swr.vercel.app - Next.js 기반 문서
- https://tailwindcss.com - Next 기반 정적 + 동적

## 7. Angular 기반 CSR
- https://angular.io
- https://material.angular.io
- https://platform.openai.com - Angular + React 혼합
- https://cloud.google.com - Angular 기반 대시보드 다수
- https://firebase.google.com

## 8. Ajax / REST / GraphQL / Infinite Scroll
- https://www.instagram.com - CSR + GraphQL + 무한스크롤
- https://www.linkedin.com/feed - React + REST + 동적 렌더링
- https://twitter.com - 완전 CSR + REST/Ajax
- https://news.ycombinator.com - 단순하지만 일부 lazy load 있음
- https://reddit.com - CSR + GraphQL

## 9. 테스트/특수 구조 사이트
- https://quotes.toscrape.com - Scrapy 튜토리얼용 SSR 사이트
- https://books.toscrape.com - 구조 분석 연습용
- https://webscraper.io/test-sites - 다양한 구조 제공
- https://httpbin.org/forms/post - POST/GET 테스트
- https://browser-info.net - 헤더/렌더링 테스트

## 10. 기업형 복합구조 사이트 (SSG+CSR+API 조합)
- https://www.apple.com - SSG 기반 + 동적 요소 일부
- https://www.microsoft.com - 동적 요소 혼합
- https://www.naver.com - 다수 iframe + JS DOM 조작
- https://www.daum.net - 동적 렌더링 일부
- https://www.coupang.com - Ajax + 무한스크롤 + 렌더링 복잡
