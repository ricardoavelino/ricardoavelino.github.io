#!/bin/bash
export PATH="/opt/homebrew/opt/ruby/bin:/opt/homebrew/lib/ruby/gems/4.0.0/bin:$PATH"
export JEKYLL_NO_BUNDLER_REQUIRE=true
cd "$(dirname "$0")"
exec jekyll _4.4.1_ serve --port 4600 --host 127.0.0.1
