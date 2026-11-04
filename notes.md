## 2026-11-04

- [ ] 2087076
- [ ] 2087049
- [ ] 1934545

## 2026-10-28

- [ ] 2011566
- [ ] 2080325

## 2026-10-21

- [ ] 2011566
- [ ] 2080325
- [ ] 1972375

## 2026-10-14

- [ ] 1894669
  - Recent-ish
- [x] 1972375
  - ESR 115
- [ ] 2007038
  - First appearance here.
  - Linux, might be related to the recent enablings from florian, although it was not explicitly disabled before.

## 2026-10-07

- [x] 2074657
  - Fixed
- [ ] 2011566
- [ ] 1767764
  - Existing flake
  - Mostly beta/etc…
  - Mostly macos1500

## 2026-09-30

- [x] 2074657
  - New
- [ ] 2011566

## 2026-09-23

- [ ] 1767786
  - Beta only

## 2026-09-16

- [x] 2071505
  - Fixed
- [x] 2020133
  - Fixed
- [x] 1767707
  - Fixed
- [ ] 2011566
  - docShell security issue
- [x] 1767786
  - Beta only
  - Ni alex to land his patch
- [ ] 1767764
  - Old intermittent, slightly spiking.

## 2026-09-09

- [ ] 1767707
- [ ] 2020133
- [x] 2009386
  - Windows asan
- [x] 2069100
  - tsan/debug/asan
  - race?

## 2026-09-02

- [ ] 1767707
  - Need to land my investigation patches
- [x] 1915308
  - Win debug
  - Patch proposed

## 2026-08-26

- [x] 2045293
  - Uplift requested
- [x] 2065002
  - Fixed
- [x] 2054163
  - Beta only
- [ ] 1767707
  - I have patches in progress but no fix so far
- [ ] 1915308
- [x] 2054192
  - Fixed

## 2026-08-19

- [x] 2045293
  - Macos 1500 only
  - Logs for adb [Bug 2065050 - Add moz log for devtools adb helpers](https://bugzilla.mozilla.org/show_bug.cgi?id=2065050)
  - Skipping [https://phabricator.services.mozilla.com/D320029](https://phabricator.services.mozilla.com/D320029)
- [x] 2054192
  - Still frequently happening on slow platforms. Maybe push with resource mozlog
  - [https://bugzilla.mozilla.org/show_bug.cgi?id=2054192#c0](https://bugzilla.mozilla.org/show_bug.cgi?id=2054192#c0)
  - Needinfo’d Nicolas
- [x] 2054163
  - Wait ?
  - Fixed!
- [ ] 1767707
  - Maybe the fixed port is already in use 6001?
  - Trying a [patch](https://phabricator.services.mozilla.com/D320043) + [push](https://treeherder.mozilla.org/jobs?repo=try&landoInstance=lando-prod-2025&landoCommitID=81384)
- [x] 1767764
  - Old issue, mac + beta

## 2026-08-12


## 2026-08-05

- [ ] 2054192
  - asan/tsan windows
- [ ] 2045293
- [ ] 1767764
  - Macos / beta

## 2026-07-29

- [ ] 2037298
- [x] 2056544
  - Closed

## 2026-07-22

- [ ] 2037298
- [x] 2056544
  - Closed

## 2026-07-15

- [x] 1972375
  - ESR
- [x] 1779172
  - Beta only
- [ ] 2037298
  - New ish
  - Macos arm only
- [x] 1767764
  - Beta only

## 2026-07-08

- [x] 1779172
  - Skipped
- [ ] 2050460
  - Has patch, waiting for

## 2026-07-01

- [ ] 1779172
- [x] 2049359
  - Fixed perma a11y
- [x] 2050460
  - new
- [ ] 1974702
- [ ] 1767737
- [x] 2049357
  - Fixed
- [ ] 1997720

## 2026-06-24

- [x] 2049359
  - Perma a11y
  - URGENT
- [ ] 1779172
- [x] 2045917
  - Beta only
  - Uplift requested
- [x] 1828919
- [x] 1830615
- [ ] 1997720
- [ ] 1974702
- [ ] 2049357
  - New
  - TSAN only

## 2026-06-17

- [x] 2047124
  - Perma a11y
  - Fixed
- [x] 2045917
  - Macos arm
  - Patch provided
- [ ] 1779172
  - Macos arm
- [x] 1832844
  - Only failed on a single day, ignoring for now
- [ ] 1830615
  - New ?

## 2026-06-10

- [ ] 1779172
  - Macos arm
- [ ] 2045917
  - New
  - Macos arm
- [ ] 1767764
  - Beta / release mostly?

## 2026-06-03

- [ ] 1779172
  - Macos arm
- [ ] 2041421
  - ???
- [ ] 1997720
  - Macos arm
- [ ] 1767737
  - Macos arm

## 2026-05-27

- [ ] 1779172
  - Macos arm
- [ ] 1767737
  - Macos arm
- [ ] 1767707
- [ ] 2020133

## 2026-05-20

- [ ] 1779172
  - Macos arm
- [ ] 1767737
  - Macos arm
- [x] 1884491
  - Potentially already fixed on beta…
- [ ] 2020133

## 2026-05-13

- [x] 2037668
  - A11y. Fixed.
- [ ] 2037805
- [ ] 1779172
- [ ] 1884491
- [ ] 2020133
- [ ] 1993826

## 2026-04-29

- [x] 2033953
  - Macos arm
  - Removing the test
- [x] 2030839
  - Fixed
- [ ] 2020133
- [x] 2032644
  - Fixed
- [x] 2035091
  - [Bug 2035205 - devtools/client/netmonitor/test/browser_net_frame.js permafails on mac](https://bugzilla.mozilla.org/show_bug.cgi?id=2035205)
- [ ] 1884491
  - Existing flake

## 2026-04-22

- [x] 2031760
- [x] 1964551
- [x] 2032384
- [ ] 2001370
- [ ] 1767716
  - Standalone
  - [Bug 2033980 - Fix debugger leak in](https://bugzilla.mozilla.org/show_bug.cgi?id=2033980) [MenuButton.js](http://MenuButton.js)
  - [https://phabricator.services.mozilla.com/D295754](https://phabricator.services.mozilla.com/D295754)
- [x] 2032644
  - Regression from waitfor
- [x] 2030839
  - Skip macos
- [ ] 2020133
- [x] 1936836
  - Same as main accessibility panel issue
- [ ] 1998960
- [ ] 1917962
- [ ] 2011566

## 2026-04-15

- [x] 2031760
  - Non devtools regression from [Bug 2026399 - Enable quad box shadows by default](https://bugzilla.mozilla.org/show_bug.cgi?id=2026399)
- [x] 2026850
  - Closed
- [x] 1815641
  - ESR 115
- [ ] 1767707
  - No answer from Alex in 3 months will disable
- [ ] 1767716
  - Standalone
  - Try 5mn if not found disable
- [x] 2001370
  - Recent spike windows only
  - Ni Nicolas
- [ ] 1917962
  - Linux opt
  - Skipped on debug http3, but current failures are not http3
- [x] 1891244
  - ESR 115
- [x] 1898695
  - Not devtools
- [ ] 1933959
  - Mostly windows, but recent spike
  - Potentially, skipping a test on windows just moves the needle to the next flake
  - But also fails on Linux with similar symptoms, albeit less frequently
- [x] 2020133
  - Hopefully fixed by [Bug 2031444 - CacheEntry pending callbacks form prevent-release cycle at shutdown, leaking nsGlobalWindowInner](https://bugzilla.mozilla.org/show_bug.cgi?id=2031444)
- [ ] 2021516
  - Try patch again
- [x] 1947368
  - ESR115
- [ ] 2029274
  - Standalone
  - Starting backfills from [https://treeherder.mozilla.org/jobs?repo=autoland&revision=c93a7ef5f55b7f0425a5e34498ee50cff0218009&selectedTaskRun=M1VoCkJwTAKoZ54bysEwfQ.0](https://treeherder.mozilla.org/jobs?repo=autoland&revision=c93a7ef5f55b7f0425a5e34498ee50cff0218009&selectedTaskRun=M1VoCkJwTAKoZ54bysEwfQ.0)
  - Try locally?
- [ ] 2029947
  - Standalone
- [x] 2027935
  - Not DevTools
- [x] 1835255
  - ESR 115
- [x] 2028688
  - Closed
- [x] 1963943
  - Moved
- [ ] 2030500
  - Still failing..
- [x] 1894899
  - ESR 140 / 115
- [ ] 2030442
  - Standalone-ish
- [ ] 1781473
  - Recent spike, mostly linux
- [x] 1982005
  - Closed
- [ ] 1984821
  - Timeout, on all platforms?
  - Not really a recent spike
- [x] 1767771
  - ESR 115
- [ ] 1979074
  - Standalone

## 2026-04-08

- [x] 1947368
  - ESR
- [x] 1982005
  - Skip on windows
- [x] 2009386
  - Try waiting for actual mutation count?
- [x] 2029273
  - Standalone frequent failure
  - disabling
- [x] 2026830
  - Trying a fix but TV only.
- [x] 1767707
  - Macos 15 beta uplift
- [x] 2026850
  - Disabling
- [x] 1973381
  - ESR
- [x] 1891244
  - ESR
- [x] 1959018
  - ESR
- [x] 2020133
  - ESR/Beta
- [x] 2023147
  - ESR
- [x] 2027498
  - Macos 15
- [x] 2028688
  - macos15
- [ ] 1767716
  - Recent regression with a leak on the debugger menu settings button
- [x] 1972034
  - ESR
- [x] 1972375
  - ESR
- [x] 1966872
  - ESR
- [x] 1775182
  - Low frequency macos intermittent
  - Proposing a patch
- [ ] 1894899
  - ESR ?
  - Not really spiking there, but just adds a few occurrences which makes this > 10 failures per week
- [ ] 1971894
  - ESR
- [ ] 1973921
  - ESR
- [ ] 1767715
  - ESR

## 2026-04-01

- [x] 1767683
  - Needs beta uplift
- [x] 2024981
  - Fixed
- [x] 1960069
  - Needs beta uplift
- [x] 1674060
  - Skipped on macos 15
- [x] 1767707
  - Skipped on macos 15
- [ ] 2021516
  - Should skip?
- [x] 2026454
  - Skipped on macos 15
- [x] 1947368
  - ESR
- [ ] 2020133
  - Recent spike? Half is on beta/esr
- [x] 1781480
  - Skipped on macos 15
- [ ] 1984821
  - Recent spike, debug only, leak.
- [x] 1781317
  - Skip
- [x] 1781499
  - Skipped on macos 15
- [x] 1959018
  - Linux TSAN ESR
- [x] 2021290
  - Fixed / skipped
- [ ] 2026850
  - New spike, windows opt?
- [ ] 1815641
  - Many beta failures?
- [x] 2023147
  - ESR
- [ ] 1982005
  - Recent spike? Windows + beta
- [ ] 2001370
  - Spike on all platforms
- [x] 1966872
  - ESR failures
- [ ] 1775182
  - ESR/beta + failing already on osx so failure count x 2
- [x] 1891244
  - ESR 115
- [x] 1894899
  - ESR
- [x] 1971894
  - ESR
- [x] 1973381
  - ESR
- [ ] 2009386
  - Recent-ish spike
- [ ] 2023887
  - Recent spike?

## 2026-03-25

- [ ] 1767707
- [x] 1960069
  - Fixed by Nicolas
- [x] 1973921
  - Spiked because of a backed out patch
- [ ] 2020133
  - Seems unrelated to devtools
- [x] 2021290
  - Disable, no update from bomsy yet
- [ ] 2021516
  - Still timing out…
- [x] 2024934
  - Perma beta sim
  - Fixed by Nicolas
- [ ] 2024981

## 2026-03-18

- [x] 1871836
- [x] 2021290
  - Bomsy on it
- [x] 2021427
  - Prepare a patch to disable on windows slow builds
- [x] 2023039
- [x] 2021481
  - Prepare a patch to disable
- [x] 1947368
  - ESR only
- [x] 1959018
  - ESR only
- [x] 2023147
  - Fixed
- [ ] 1767707
  - Not sure, a bit flaky, low volume, regular intermittent
- [x] 1781317
  - Flaky, update expectations to cover asan/tsan/ccov
- [x] 1971894
  - ESR only
- [x] 1973921
  - ESR only
- [x] 1972034
  - ESR only

## 2026-03-11

- [ ] 1871836
  - Failing on all platforms since last week?
  - Maybe from [https://bugzilla.mozilla.org/show_bug.cgi?id=2014623](https://bugzilla.mozilla.org/show_bug.cgi?id=2014623) ?
  - Nope
  - [LIST OF NECKO BUGS -14d](https://bugzilla.mozilla.org/buglist.cgi?chfieldfrom=-14d&chfieldvalue=RESOLVED&component=Networking&component=Networking%3A%20Cache&component=Networking%3A%20Cookies&component=Networking%3A%20DNS&component=Networking%3A%20File&component=Networking%3A%20HTTP&component=Networking%3A%20JAR&component=Networking%3A%20Proxy&component=Networking%3A%20WebSockets&classification=Client%20Software&classification=Developer%20Infrastructure&classification=Components&classification=Server%20Software&classification=Other&list_id=17881299&product=Core&resolution=FIXED&query_format=advanced&chfield=bug_status)
  - Maybe [Bug 1930738 - Consider not lowering the request priority of images with the LOAD_BACKGROUND flag](https://bugzilla.mozilla.org/show_bug.cgi?id=1930738) ?
- [x] 2021290
  - Linux debug only?
  - Potentially from [Bug 2015281 - Migrate getExpressionVariables to CM6](https://bugzilla.mozilla.org/show_bug.cgi?id=2015281)
  - Confirmed -> Bomsy should fix
- [x] 2021481
  - Windows only?
  - Maybe [https://bugzilla.mozilla.org/show_bug.cgi?id=2020268](https://bugzilla.mozilla.org/show_bug.cgi?id=2020268)
- [x] 2021427
  - Windows only as well
  - Maybe [https://bugzilla.mozilla.org/show_bug.cgi?id=2020268](https://bugzilla.mozilla.org/show_bug.cgi?id=2020268)
- [x] 1947170
- [x] 2021516
  - Windows asan / debug
- [ ] 1811903
  - Spiking a bit due to additional macos workers?
- [ ] 2009386
  - Windows asan? Windows performance issue?
- [ ] 1998960

## 2026-03-04

- [ ] 1767694
- [x] 1947170
  - ESR Spike
- [x] 1966872
  - ESR Spike
- [ ] 2006111
  - Not sure still
- [x] 2011566
  - Disable on all linux slow platforms

## 2026-02-25

- [ ] 2016837
  - Retriggers from [https://treeherder.mozilla.org/jobs?repo=autoland&selectedTaskRun=YO8-1YJeQGy2XKSnEuWVNQ.0&tochange=98c6a22fd4c386bdc523285c68479e3f6440be80&fromchange=27091df8a49091212b71c34b22e4498b50c1fa96](https://treeherder.mozilla.org/jobs?repo=autoland&selectedTaskRun=YO8-1YJeQGy2XKSnEuWVNQ.0&tochange=98c6a22fd4c386bdc523285c68479e3f6440be80&fromchange=27091df8a49091212b71c34b22e4498b50c1fa96)
  - Windows asan only
  - SQLite issues?
- [ ] 2011566
  - Now popping up on slow platforms in general (asan, ccov)
  - Back on > 10 mostly because of a surge of ccov

## 2026-02-18

- [x] 1767637
  - ESR 140 only
  - Proposing to uplift [Bug 1981465 - Handle timings = 0ms devtools/client/netmonitor/test/browser_net_columns_time.js](https://bugzilla.mozilla.org/show_bug.cgi?id=1981465)
- [ ] 1890108
  - ???
- [x] 1966872
  - ESR 140 only
- [ ] 1998960
  - Just flaky by nature, bad test
- [x] 2016406
  - Perma, fixed

## 2026-02-11

- [ ] 1767731
  - Issue with ETP
- [ ] 1767733
  - Issue with ETP
- [ ] 1947170
  - Sometimes spikes on beta / later
- [x] 1987665
  - Wait: true
- [ ] 2006111
  - Trying a few things, but if it all fails we should disable on macos debug I guess
- [x] 2013722
  - Maybe screenshots ?
  - Try to disable screenshots during the tests
  - Otherwise skip on windebug

## 2026-02-04

- [ ] 1767707
  - Will disable
- [ ] 2011566
  - Skipped
- [ ] 2013722
  - Maybe screenshots ?
  - Otherwise skip on windebug

## 2026-01-28

- [ ] 2011566
  - Will disable
- [ ] 2012028
  - Skip on opt?
- [ ] 2009123
  - Meh

## 2026-01-21

- [x] 1980013
  - Still failing need to check the logs
- [x] 1910261
  - Maybe skip linux asan for _browser_console.toml
- [x] 1927821
  - New entry
  - Almost windows debug only
  - Let’s try to fix the test
- [x] 1767707
  - Still have a need info on Alex
  - Lots of skip ifs removed a few month ago, will restore linux debug one.
- [x] 1966744
  - Linux debug
  - [11] [Bug 1894899 - Intermittent devtools/client/storage/test/browser_storage_cache_navigation.js | single tracking bug](https://bugzilla.mozilla.org/show_bug.cgi?id=1894899)
  - Same issue ?
- [x] 1998960
  - Those tests are depressing.

## 2026-01-14

- [ ] 1767707
  - Asked info from Alex
- [ ] 1980013
  - Still frequently failing on mac opt
  - Providing a patch to log a string after the failure
- [ ] 1998960
  - ?

## 2026-01-07

- [ ] 1767637

## 2025-12-31

- [ ] 1947170
- [ ] 1996490

## 2025-12-24

- [ ] 1996490
- [ ] 1767707
- [ ] 1995989

## 2025-12-17

- [ ] 1781497
- [ ] 1996490
- [ ] 1997758

## 2025-12-10

- [ ] 1996490

## 2025-12-03

- [x] 2001915
  - Already fixed

## 2025-11-26

- [ ] 1892570
- [ ] 2001915
- [ ] 1996490
- [ ] 1767707
- [ ] 1767637

## 2025-11-19

- [x] 1995762
  - Need to find a real fix
- [ ] 1998960
  - Slightly spiking
- [x] 1796185
  - Already fixed…
- [x] 1767637
  - ESR
- [ ] 1997758
  - Macos only, recent-ish spike

## 2025-11-12

- [x] 1991020
  - Fixed
- [ ] 1995762
  - Still failing

## 2025-11-05

- [x] 1947368
  - Porting the 1804 annotation over, but failing mostly on beta esr
- [x] 1995762
  - Added a small wait, but not sure that will actually fix it…
- [ ] 1767707

## 2025-10-29

- [ ] 1767786
- [x] 1812593
  - Skip if restored
- [x] 1901580
  - Proposed a fix
- [x] 1991373
  - Pinged nicolas

## 2025-10-22

- [x] 1812593
  - Forgot to ask for review…
- [ ] 1991373
  - Leak :/

## 2025-10-15

- [x] 1812593
  - Let’s skip on linux debug as well, it’s already skipped on opt
- [x] 1767707
  - Skip if restored
- [x] 1872980
  - Fixed
- [ ] 1991373
  - Leak :/

## 2025-10-08

- [x] 1767778
  - Restore skipif
- [x] 1767707
  - Restore skipif
- [ ] 1991373
- [x] 1781317
  - Update skipifs
- [ ] 1812593
- [x] 1767637
  - Seems to spike on esr140 ?
- [x] 1872980
  - A11y crap
  - Asked Nicolas to take a look
- [x] 1966872
  - Beta / esr
- [ ] 1767786
  - Still waiting for feedback from alex
- [x] 1980013
  - Meh

## 2025-10-01

- [x] 1990463
  - A11y perma/fixing
- [x] 1990459
  - Perma/regression. Fixed
- [x] 1990541
  - Same issue as [Bug 1767686](https://bugzilla.mozilla.org/show_bug.cgi?id=1767686) ?
  - Nicolas looking at it
- [x] 1966872
  - Disabled on windows asan
- [x] 1948043
  - Fixed by Alex
- [ ] 1812593
- [ ] 1781317
- [ ] 1927128
  - Moved to [Bug 1991373 - Intermittent leakcheck large SystemGlobal | devtools/client/webconsole/test/browser/_browser_console.toml | single tracking bug](https://bugzilla.mozilla.org/show_bug.cgi?id=1991373)
  - Windows MSIX only, but unless we skip the whole suite, there’s not much we can do about this
- [x] 1767637
  - ESR 140 failures, was fixed in 143
- [x] 1767786
  - Maybe we should not assert objects without stack
- [x] 1947170
  - Only seems to fail on ESR/Release.
- [ ] 1985681
  - Spiked on 26
- [x] 1781497
  - Mistriaged from recent beta perma.
- [x] 1949036
  - Fixed by Holger

## 2025-09-24

- [x] 1949036
- [x] 1767686
- [ ] 1948043
- [x] 1966872
- [x] 1118592
  - Maybe skip on linux opt again?
- [ ] 1812593
- [ ] 1980013

## 2025-09-17

- [ ] 1767686
- [x] 1904034
- [ ] 1948043
- [ ] 1949036

## 2025-09-10

- [x] 1904034
- [x] 1980334
  - Skipped
- [ ] 1948043
- [ ] 1767686
- [ ] 1980013

## 2025-09-03

- [x] 1948043
  - Some new failures from [Bug 1980617 - "Switch to tab/group" no longer scrolls tab strip to show active tab when it belongs to a tab group](https://bugzilla.mozilla.org/show_bug.cgi?id=1980617)
- [x] 1904034
  - Ni’d  bomsy
  - Spike started on 26th of august
- [ ] 1767686
  - Spike started on 26th of august
- [x] 1955603
  - Skipping
- [ ] 1980013
- [x] 1767707
  - Was recently re-disabled
- [ ] 1985681
  - Spike started on 26th of august
- [ ] 1860923
- [ ] 1966872
- [x] 1973381
  - Skip ifs have been updated

## 2025-08-27

- [x] 1984832
- [ ] 1948043
- [ ] 1767707
- [ ] 1973381
- [x] 1984562
- [ ] 1860923
- [ ] 1980013
- [ ] 1947368
- [ ] 1812593
- [ ] 1889134
- [ ] 1955603

## 2025-08-20

- [ ] 1948043
- [ ] 1767707
- [ ] 1860923

## 2025-08-13

- [ ] 1966872
- [ ] 1980013
- [ ] 1948043
- [x] 1973381
- [ ] 1860923
- [ ] 1767707
- [x] 1947368
- [ ] 1979660
- [ ] 1955603
  - Linux tsan only

## 2025-08-06

- [x] 1971894
  - Disabled last week, only failing on beta / esr / …
- [x] 1973381
  - Disabled last week, only failing on beta / esr / …
- [ ] 1966872
- [x] 1840923
  - New?
- [ ] 1948043
- [x] 1980013
  - Disabled last week, only failing on beta / esr / …
- [x] 1979074
  - Disabled last week, only failing on beta / esr / …
- [x] 1947368
  - Disabled last week, only failing on beta / esr / …
- [ ] 1767707
- [ ] 1979660
- [x] 1767637
  - Trying something
- [ ] 1781323
- [ ] 1977040

## 2025-07-30

- [x] 1971894
- [x] 1973381
- [ ] 1947368
- [ ] 1966872
- [x] 1979074
- [ ] 1948043
- [ ] 1767637
- [ ] 1781317
- [ ] 1840923
- [ ] 1781328

## 2025-07-23

- [ ] 1971894
- [ ] 1973381
- [ ] 1966872
- [ ] 1947368
- [x] 1898415
- [ ] 1978093
- [ ] 1781323
- [ ] 1781328
- [ ] 1767779
- [ ] 1767707

## 2025-07-16

- [ ] 1971894
- [ ] 1966872
- [ ] 1973381
- [x] 1781328
- [x] 1767779
- [x] 1781323
- [ ] 1947368
- [x] 1898415
- [ ] 1948043
- [ ] 1812593
- [ ] 1860923
- [ ] 1767779
  - ??? rarely failing
- [ ] 1972034
- [ ] 1973921
- [x] 1975120
- [x] 1975131

## 2025-07-09

- [x] 1975120
  - Will be temporarily disabled
- [x] 1975131
  - Will be temporarily disabled
- [x] 1971894
  - Trying to trigger updates from the test?
- [x] 1973381
  - Trying to trigger updates from the test?
- [ ] 1966872
- [ ] 1767655
- [ ] 1767692
- [ ] 1898415
- [ ] 1607636
- [ ] 1973972
- [ ] 1812593
- [ ] 1567800
- [ ] 1781323
- [ ] 1948043
- [ ] 1781328
- [ ] 1811903
- [ ] 1889134
- [ ] 1959018

## 2025-07-02

- [ ] 1971894
  - 50% of failures from beta or esr
- [x] 1607636
  - Should be fixed, remaining failures on beta
- [ ] 1973381
  - 50% of failures from beta or esr
- [ ] 1966872
  - 50% of failures from esr / beta
- [x] 1897912
  - Skipping on linux 1804 tsan
- [ ] 1767692
- [ ] 1973972
- [ ] 1781323
- [ ] 1948043
- [ ] 1781471
- [x] 1973006
- [ ] 1937308
- [ ] 1947368

## 2025-06-25

- [x] 1607636
- [ ] 1767692
- [ ] 1767695
- [ ] 1897912
- [ ] 1966872
- [ ] 1971894
- [ ] 1973006
- [ ] 1973381
- [ ] 1973616

## 2025-06-18

- [ ] 1767692
- [ ] 1767695
- [ ] 1781317
- [ ] 1812593
- [ ] 1947368
- [ ] 1966872
  - Still high because of beta, monitor for next week
- [ ] 1971894
  - Still high because of beta, monitor for next week
- [ ] 1781479
  - Still high because of beta, monitor for next week
- [x] 1965340
  - Fixed
- [x] 1767688
  - Fixed
- [x] 1432301
  - Throttled parent process resources
- [x] 1971598
  - Throttled parent process resources
- [x] 1971632
  - Throttled parent process resources
- [x] 1971820
  - Throttled parent process resources
- [x] 1972170
  - Throttled parent process resources
- [x] 1904942
  - Throttled parent process resources

## 2025-06-11

- [ ] 1767692
- [ ] 1947368
- [ ] 1948043
- [ ] 1812593
- [ ] 1781497
- [x] 1767772
- [x] 1767688
- [x] 1947358
- [x] 1781479
- [x] 1950845
- [x] 1965340
- [x] 1966872
- [x] 1970057

## 2025-06-04

- [x] 1966872
- [ ] 1947368
- [ ] 1767688
- [ ] 1767772
- [ ] 1781323
- [ ] 1950845
- [ ] 1812593
- [ ] 1897912
- [ ] 1781497
- [x] 1781479
- [x] 1947358
- [x] 1958918
- [x] 1965340
  - Fixed
- [x] 1970057
  - Fixed

## 2025-05-28

- [ ] 1965340
- [ ] 1781479
- [ ] 1966872
- [ ] 1947358
- [ ] 1947368
- [ ] 1812593
- [x] 1966826

## 2025-05-21

- [ ] 1965340
- [ ] 1947358
- [ ] 1947368
- [ ] 1966872
- [ ] 1767772
- [ ] 1812593
- [ ] 1959018
- [ ] 1607636
- [ ] 1767692
- [ ] 1767688
- [ ] 1894312
- [x] 1966826
  - Fix submitted
- [x] 1961617
  - Fix proposed
- [x] 1952608
  - Fixed

## 2025-05-14

- [ ] 1952608
  - Frequently failing, asan only -> skip
- [ ] 1947358
  - Service worker issue
- [ ] 1767772
- [ ] 1767688
  - Mostly windows beta failures
- [ ] 1947368
  - Try to wait for the element
  - Otherwise should disable on debug asan tsan
  - This test only seems to run fin on windows opt for some reason
  - Waiting for try again
- [ ] 1767692
  - Still frequently failing no idea what’s wrong with this DPR test
- [ ] 1812593
  - Only failing on regular opt builds apparently, trying to make the close a bit more reliable…
- [ ] 1781479
  - Service worker issue
- [ ] 1949050
  - TSAN timeout
- [ ] 1950845
- [ ] 1959018
- [ ] 1897912
- [ ] 1942027
- [x] 1929339
  - Fixed
- [x] 1607636
  - Most failures on beta where skip if is not applied

## 2025-05-07

We still have the regression from last week which is not fixed + another bug which spiked a lot

- [x] 1952608
  - On autoland
- [ ] 1929339
  - Regression from [Bug 1956753 - Highlight the selected trace line in CodeMirror](https://bugzilla.mozilla.org/show_bug.cgi?id=1956753)
  - Alex is ni’d
- [ ] 1947358
  - In several failures I can see an issue in destroy?
- [ ] 1781479
- [ ] 1767692
- [ ] 1767772
- [ ] 1952608
- [ ] 1607636
- [ ] 1947368
- [ ] 1767688
- [ ] 1949050

## 2025-04-30

There’s been a high frequency regression which failed a lot for a few days. So for regular intermittents the figure is actually low.

- [ ] 1963212
- [ ] 1947358
- [ ] 1607636
- [ ] 1767692
- [ ] 1767772
- [ ] 1781479
- [ ] 1808555
- [ ] 1960679
- [ ] 1767727
- [ ] 1767688

## 2025-04-23

Easter weekend so maybe less pushes than usual

- [ ] 1767692
  - Still failing a lot even after adding skipifs
- [ ] 1767727
  - New
- [ ] 1767772
  - Still frequently failing on mac opt
- [ ] 1781479
  - Still failing
- [ ] 1923756
  - Skipped on mac, now rarely failing on linux opt
- [ ] 1947358
  - Still failing
- [ ] 1947368
- [x] 1959055
  - Trying a fix
- [x] 1960679
  - Recent regression from Bug 1835264
  - Fixed
- [x] 1767735
  - Fixed
- [x] 1607636
  - Skipping
- [x] 1767273
  - Fixed, only failures on beta
- [x] 1889524
  - Fixed

## 2025-04-16

Still dealing with the fallout from [Bug 1957258 - cleanup devtools-chrome .toml files](https://bugzilla.mozilla.org/show_bug.cgi?id=1957258)

- [ ] 1607636
  - Still failing frequently on linux tsan opt
  - Let’s improve logs already
- [ ] 1781479
  - From mass enabling, was skipped on many platforms (asan, debug, tsan)
- [ ] 1889524
  - Not clear, reproduced once locally
  - Only failing on macos debug
- [ ] 1947358
  - From mass enabling most likely, maybe the same issue as [https://bugzilla.mozilla.org/show_bug.cgi?id=1781479](https://bugzilla.mozilla.org/show_bug.cgi?id=1781479) above?
- [ ] 1863103
  - Frequently failing on linux tsan
- [ ] 1781497
  - From mass enabling, ni to :mak
  - Trying a patch on the implementation
  - Actually re-disabled but would still like to investigate
- [x] 1767772
  - Added back skip ifs
- [x] 1767692
  - Added back skip-ifs
- [x] 1767707
  - Added back skip-ifs
- [x] 1767273
  - Skipped
- [x] 1889407
  - Fixed
- [x] 1781471
  - Added back skip-ifs
- [x] 1817966
  - Added back skip-ifs
- [x] 1767662
  - Skipping
- [x] 1767768
  - Skipped an assert
- [x] 1767691
  - Fixed
- [x] 1787011
  - Mostly windows asan
  - Might be from mass enabling, not sure
- [x] 1958748
  - Skipped + fix proposed by Alex
- [x] 1767724
  - From mass enabling because we no longer skip webconsole tests on asan, so failures slightly spiked
  - Looks like nothing happens when clicking on the clear button as the UI still shows all messages displayed.
  - Ni on Nicolas, waiting seems to fix the issue.
- [x] 1959062
  - Skipped
- [x] 1767771
  - Added back skip-ifs
- [x] 1954964
  - Throttling in quick-open makes the test fail
  - Mostly linux debug
- [x] 1767769
  - Linux asan
- [x] 1767633
  - Fixed

## 2025-04-09

There was a mass enabling of disabled tests in [Bug 1957258 - cleanup devtools-chrome .toml files](https://bugzilla.mozilla.org/show_bug.cgi?id=1957258) so it’s not entirely surprising, but will take time to cleanup

- [x] 1767692
  - The whole test suite was skipped on windows, this particular test was also skipped on linux debug. It now frequently fails on linux debug + win h2. But it was already failing quite frequently considering how many platforms it runs on.
  - Trying to wait properly for DPR to be updated? The clicks seem to occur at a multiple of the expected value …
  - Doesn’t work
  - Restore skip on windows and linux debug
- [ ] 1767273
  - Many failures from beta
  - Timing out waiting for a event timings + payload, is a request not finishing properly?
  - There is a XML parsing error on a sjs file, almost debug only
- [x] 1767772
  - Many failures on linux asan
  - Many failures from beta
  - Restore skip for linux asan
- [x] 1767707
  - Restore skip for linux debug
- [ ] 1767662
  - Many failures on beta
  - Macos only
  - Looks like an issue on the test server with the WS backend file?
- [ ] 1889407
  - Trying a fix for macos, otherwise let’s skip it
  - Not related to mass enabling
- [ ] 1607636
  - Failing on linux tsan and linux opt
  - Not necessarily related to mass enabling
- [x] 1781471
  - Adding back relevant skip ifs
- [ ] 1863103
  - Spiked on linux tsan be[https://bugzilla.mozilla.org/show_bug.cgi?id=1863103](https://bugzilla.mozilla.org/show_bug.cgi?id=1863103)fore the mass enabling. Might be due to a race in the helper to wait for virtualized messages.
  - Could skip on linux tsan
  - Will try a fix
- [x] 1767735
  - Fixed by Nicolas !
- [ ] 1923756
  - Fails often on linux tsan
  - mass enabling was for linux debug http3
  - Could add a different skip? But the linux debug http3 failure might just come back as well?
- [x] 1767633
  - Usually timing out waiting for more and more event timings.
  - Test seems racy, trying a fix
- [ ] 1947358
  - Was reenabled on tsan, but the most frequent failure is macos debug for now.
  - Could skip there
- [x] 1958748
  - Restore skip for macos debug
- [ ] 1767691
  - From mass enabling, could restore more selective skips, but want to try a fix as well
- [ ] 1767768
  - Might be slightly more frequent from mass enabling, but there’s an issue on slow platforms
  - Proposed a patch, but should be discussed
- [x] 1781497
  - Restoring skip ifs
- [x] 1767771
  - Restoring skip ifs
- [x] 1767758
  - Adding win asan skip if
- [ ] 1767764
- [x] 1959062
  - Restoring skip if
- [x] 1817966
  - Restoring skip-ifs
- [x] 1767778
  - Proposing a fix

## 2025-04-02

- [ ] 1432176
- [ ] 1767273
- [ ] 1767735
- [ ] 1812593
- [ ] 1889407
- [ ] 1947358

## 2025-03-26

starting this week I will track all intermittents with more than 10 failures to align with the spreadsheet. We also are close to 10 bugs any way

- [x] 1955976
  - Fixed
- [ ] 1767735
  - Same as previous weeks
- [ ] 1889407
  - Still failing only on macos
- [ ] 1767633
  - Same as previous weeks
- [ ] 1432176
  - Lots of investigations on this old bug
  - Failing on linux asan
- [ ] 1929339
- [x] 1955997
  - Fixed
- [x] 1767658
  - Fixed, only failing on beta now.
- [x] 1767668
  - Macos debug only
  - Shape is not correct
  - Looks like we still show the previous polygon clip path, maybe a bug on the server where we actually erase the value?
  - Can’t reproduce locally
  - I think extracting the test to a dedicated task should fix it.
- [ ] 1781317
  - Linux asan only, maybe we should wait for the worker registrations correctly
  - Waiting doesn’t seem to cut it?
- [ ] 1812593
  - TODO
- [ ] 1947358
  - New-ish. Was very frequent on tsan, now still failing a bit on debug builds

## 2025-03-19

- [ ] 1432176
  - New in top 10
  - Linux asan and tsan
- [ ] 1767633
  - Still timing out missing on an event timing
- [x] 1767658
  - Seems fixed, only failures on beta now.
- [ ] 1767692
  - Recent spike
  - 50% failing on beta
- [ ] 1767735
  - Still frequently failing, lots of failures coming from beta.
- [x] 1767781
  - Seems fixed
- [ ] 1783639
- [ ] 1889407
- [ ] 1929339
- [ ] 1951769

## 2025-03-12

- [x] 1767656
  - Patch submitted
- [x] 1767658
  - Should be fixed by [Bug 1953516 - Network monitor is not fetching timings for totalTime = 0 requests](https://bugzilla.mozilla.org/show_bug.cgi?id=1953516)
- [ ] 1767735
  - Same as last week
- [x] 1767781
  - Still failing quite frequently, should probably restore the skip ifs
- [x] 1783639
  - macos only
  - Let’s skip on this OS
- [ ] 1889407
  - Beta spike
  - macos only
- [x] 1923756
  - Disabled
- [x] 1929339
  - Beta spike
  - Should be out of top intermittents thanks to [Bug 1952036 - Make waitFor condition safer in browser_dbg-javascript-tracer-sidebar-values-search.js](https://bugzilla.mozilla.org/show_bug.cgi?id=1952036)
- [x] 1932503
  - Recent spike
  - Linux debug only
  - Fix submitted
- [x] 1951769
  - Intermittently passing on a11y checks
  - Skip

## 2025-03-04

- [x] 1767721
  - Usually skipped on windows, but the os version is different on the most recent windows platforms.
  - Seems easy to fix locally?
- [ ] 1767735
  - Grid element is removed but grid list not updated.
  - Probably an implementation issue, looks like we are missing a mutation in this case.
- [ ] 1767771
  - Still failing relatively frequently on linux debug, was already disabled on linux + http3 and windows
- [x] 1767781
  - Recurring entry, skipped almost everywhere, still failing on asan.
  - Let’s try to split the test and isolate the failing part.
- [ ] 1783639
  - Failing almost exclusively on macos
- [x] 1808555
  - Failing only on linux debug
  - Skipping on this platform
- [x] 1923756
  - Disabled by sheriffs
- [ ] 1924831
  - Failing mostly on linux debug
- [x] 1929339
  - Fails only on debug
  - Landed a fix to reduce the frequency, let’s monitor
- [x] 1946860
  - Fix landing

## 2025-02-21

- [x] 1831388
  - Fixed
- [ ] 1923756
- [ ] 1767781
  - Asan only, but it’s virtually skipped everywhere else…
- [x] 1767701
  - Beta/Release only, probably CM5 only. Should be out of the list soon
- [ ] 1812593
  - Fails on various platforms
- [ ] 1946860
  - Old test but recent intermittent, might be linked to recent performance changes on the network monitor?
- [ ] 1924831
  - Test timing out mostly on linux debug
- [ ] 1929339
  - Debug only
- [ ] 1767771
  - Debug only, linux.
- [ ] 1767735
  - Full test timeout, no information.
  - All platforms

## 2025-02-17

- [ ] 1923756
  - Half of the failures are from beta
- [ ] 1889162
  - Asan, tsan, debug
- [ ] 1767735
  - No clear pattern for failures (all builds, all platforms)
- [x] 1947368
  - Leftover from [https://bugzilla.mozilla.org/show_bug.cgi?id=1767698](https://bugzilla.mozilla.org/show_bug.cgi?id=1767698) mostly fails on beta/release/esr. Should be gone from top intermittents soon
- [x] 1946333
  - Misclassified
- [x] 1767701
  - Beta/Release only, probably CM5 only. Will be out of the list soon
- [ ] 1767633
  - Mostly asan failures. Timeout missing an event timing: EventTimings: 1698/1699
- [ ] 1767781
  - Asan only, but it’s virtually skipped everywhere else…
- [ ] 1767778
  - Half of failures are from tsan on release, rest is debug autoland. Frequency will decrease soon
- [ ] 1812593

## 2025-02-07

- [x] 1945519
  - Skipped
- [x] 1945533
  - A11y, Nicolas is working on a fix I think?
  - Confirmed, will be fixed by twisty-update
- [x] 1946102
  - Closed already
- [x] 1945327
  - Closed already
- [x] 1945849
  - Closed already
- [ ] 1607636
  - Reenabled, mostly failing on beta
  - To monitor
- [x] 1945200
  - Closed already
- [x] 1767696
  - Mostly tsan, should disable
- [ ] 1923756
  - Still frequently failing
- [ ] 1889162
  - Asan, tsan, debug. Maybe a race?

## 2025-01-31

- [x] 1830888
  - [julian] Only fails on mac OS, let’s skip on mac. [phab](https://phabricator.services.mozilla.com/D236324)
  - SKIPPED
- [x] 1767701
  - [julian] Only fails on beta/release. Probably CM5 related. Let’s wait for CM6 to ride the trains
- [ ] 1766133
  - [julian] Leak, mostly windows debug. Some non-devtools failures get classified in this one as well. But 90% of the failures are devtools. Should first find a smaller test case to repro. Can’t disable anything here.
  - Easy to repro with devtools/server/tests/browser/browser.toml
- [x] 1767778
  - [julian] Disabled on tsan, only still failing on beta, should soon be out of the top intermittents
- [x] 1936634
  - [julian] Fails mostly on linux debug, let’s skip.
  - SKIPPED
- [x] 1924993
  - [julian] Linux debug only, but maybe this is an input focus issue? Trying [https://treeherder.mozilla.org/jobs?repo=try&revision=f44c5547442264529071a3e658d1b966611340fb](https://treeherder.mozilla.org/jobs?repo=try&revision=f44c5547442264529071a3e658d1b966611340fb)
  - Actually we manage to write “foo” in the input but it gets deleted right after.
  - Patch submitted, but we might find something better.
  - Fixed by Bomsy
- [ ] 1767771
  - [julian] Debug only, linux and windows. We seem to miss a reflow related to an iframe. I tried to improve the test a bit but no luck so far.
- [x] 1891110
  - [julian] Failures on many platforms, for many reasons. I think we get random requests eg `[http://127.0.0.1:8888/safebrowsing4-dummy/update&$req=ChUKE25hdmNsaWVudC1hdXRvLWZmb3gaCggFEAEiAiACKAEaCggBEAEiAiACKAEaCggDEAEiAiACKAEaCggHEAEiAiACKAEaCggJEAEiAiACKAE=](http://127.0.0.1:8888/safebrowsing4-dummy/update&$req=ChUKE25hdmNsaWVudC1hdXRvLWZmb3gaCggFEAEiAiACKAEaCggBEAEiAiACKAEaCggDEAEiAiACKAEaCggHEAEiAiACKAEaCggJEAEiAiACKAE=)` polluting the test.
  - Patch submitted.
- [ ] 1923756
  - [julian] Fails on Linux and macos, opt and debug.
- [x] 1767698
  - [julian] Mostly linux asan, waiting for the animation inspector element doesn’t work.
  - SKIPPED
