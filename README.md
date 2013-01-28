pysiphash
====

A Python implementation of [SipHash-2-4](https://131002.net/siphash/),
a fast short-input
[PRF](https://en.wikipedia.org/wiki/Pseudorandom_function) with a
128-bit key and 64-bit output.

Extract from the description:

    SipHash is a family of pseudorandom functions (a.k.a. keyed hash
    functions) optimized for speed on short messages.

    Target applications include network traffic authentication and defense
    against hash-flooding DoS attacks.

    SipHash is secure, fast, and simple (for real):
    * SipHash is simpler and faster than previous cryptographic algorithms
      (e.g. MACs based on universal hashing)
    * SipHash is competitive in performance with insecure
      non-cryptographic algorithms (e.g. MurmurHash)
    * We propose that hash tables switch to SipHash as a hash
      function. Users of SipHash already include OpenDNS, Perl 5, Ruby, or
      Rust.

`Pysiphash` is tested on Python 2.7 and Python 3.2.

Introductory blog post: https://idea.popcount.org/2013-01-24-siphash/

installation
----

Released `pysiphash` versions are available on
[pypi](http://pypi.python.org/pypi/siphash/). To install it use
`easy_install` or `pip`:

    $ pip install siphash

or

    $ easy_install siphash

usage
----

`Pysiphash` tries to follow the
[hashlib](http://docs.python.org/2/library/hashlib.html) API. You can
add data to the hash by calling an `update` method, or feed data
directly to the constructor:

```python
>>> import siphash
>>> key = '0123456789ABCDEF'
>>> sip = siphash.SipHash_2_4(key)
>>> sip.update('a')
>>> sip.hash()
12398370950267227270L

>>> siphash.SipHash_2_4(key, 'a').hash()
12398370950267227270L
```

To extract the hash as a numeric value call `hash()`:

```python
>>> siphash.SipHash_2_4(key, 'a').hash()
12398370950267227270L
```

Or `digest()` to get a raw 8-bytes string:
```python
>>> siphash.SipHash_2_4(key, 'a').digest()
'\x86L3\x9c\xb0\xdc\x0f\xac'
```

Or `hexdigest()` for a 16-bytes hex encoding:
```python
>>> siphash.SipHash_2_4(key, 'a').hexdigest()
'864c339cb0dc0fac'
```

testing
----

A series of sanity checks are present inline the main `pysiphash`
code, to run it type:

    $ python siphash/__init__.py
    all tests ok

speed
----

Currently `pysiphash` is a pure-python code, so don't expect blazing
speed. On my machine computing a hash from a ten byte string takes
around 0.31 ms, and hashing 1MiB blob takes 770 ms.
