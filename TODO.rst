TODOs
=====

#) Features
    - support of ssh distribution with pytest-xdist

      - run purkinje server on external network interface?

    - Dektop notifications (optional)

    - filter by pytest.mark information

    - Acoustic signal when suite fails (configurable)

      - speech synthesis (Chrome only):
        - http://html5-examples.craic.com/google_chrome_text_to_speech.html

    - drivers for other test frameworks (nose? golang? karma? ...)

    - Configurable UI update frequency to avoid high load

#) Testing

    - test cases for WebSocket endpoint(s)

    - Move test config files to subdirectory

    - show badge with test coverage(of purkinje project) on github?

#) Continuous integration

    - Configure and activated coveralls

#) Code

    - verify each JS file uses strict mode

    - set purkinje.__version__ and use it in setup.py

    - Make debug mode configurable (to affect debug logging,
      asset concatenation and compression)

    - Use controllerAs syntax in Angular templates (?)

    - Remove obsolete CSS classes

    - py.test & py.test does not work correctly xdist (-n 2):
      - test results get recorded (all?)
      - no doughnut charts (because no suite-finished event? Investigate)
      - session start and session terminated messages arrive twice

    - heed John Papas style guide

    - provide Modernizr as a service; add Modernizr checks


#) User Interface

   - height of results table should take available vertical space

   - Better looking replacement for vanilla HTML title tooltips

   - Chartjs tooltips are cut off at the border of the canvas;
     see https://github.com/nnnick/Chart.js/issues/622

   - show tag counts?

   - show nav menu when view is too narrow

   - show error when WebSocket communication is blocked by proxy
     20150516: only shows 'Disconnected' icon. Console shows error
     in angular-reconnecting-websocket.js:124

   - Better looking idle state with no data?

#) Performance

    - YSlow / PageSpeed checks

#) Documentation

    - Sphinx, Read The Docs

    - sphinxcontrib.autohttp.flask

    - JS API documentation

    - Animated gif for README (mini screencast)?

#) Build

    - "manage.py assets check" raises Exception AttributeError: "'Environment' object has no attribute 'environment'"

#) Deployment

    - Docker container? (+ fig?)

    - Vagrant file?

#) Publishing

    - register with (`py.test web page <http://pytest.org/latest/plugins_index/index.html?highlight=plugins>`_)
      and / or `  py.test plugs <http://pytest-plugs.herokuapp.com/>`_

#) Packaging

    - split out docformat testing(plugin)?

#) First release prerequisites

    - Authentication (API key)
      to restrict access for running tests
      (optional?)

    - Authentication for web interface
      (optional)

    - start/stop script (like sentry)?

    - Minify & concatenate assets

      - application config file: debug parameter to
        control minification

    - Domain name?

    - nginx @ port 80; Demo under /purkinje_demo?

    - Minimal but sufficient documentation on how to configure py.test with purkinje

    - Update requirements.txt flotsam purkinje*/pytest-purkinje dependencies to use
      actual release versions

    - Should receive messages (test results) when not on dashboard page


Issues
======

- Memory leak in Chrome:

    becomes obvious when sending many
    WebSocket messages to browser:

    - only seems to go away when closing tab

    - see Chrome dev tools(timeline and profiles / heap snapshot)

    - still an issue?

- Coverage reports for greenlets are incorrect(see https: // bitbucket.org / ned / coveragepy / issue / 149 / coverage -
  gevent - looks - broken)

    - Option "concurrency = gevent" to coverage does no longer seem to exist
