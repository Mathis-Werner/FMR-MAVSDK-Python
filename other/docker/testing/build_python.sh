#!/bin/bash

#
# Helper for building python versions
#
# Based on https://github.com/xvzf/tox-docker/blob/master/build_python.sh
#


gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \


function clean_pyc {
    find /usr/local -depth \
    \( \
        \( -type d -a \( -name test -o -name tests \) \) \
        -o \
        \( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
    \) -exec rm -rf '{}' +
}


# Install python
for PYTHON_VERSION in $PYTHON_VERSIONS; do

    cd /tmp

    # Get source
    wget -O "python_${PYTHON_VERSION}.tar.xz" \
       "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-${PYTHON_VERSION}.tar.xz"


    # Extract source
    mkdir -p "/usr/src/python_${PYTHON_VERSION}"
    tar xJC "/usr/src/python_${PYTHON_VERSION}" --strip-components=1 \
        -f python_${PYTHON_VERSION}.tar.xz

    rm "python_${PYTHON_VERSION}.tar.xz"


    # Configure, build and install
    cd "/usr/src/python_${PYTHON_VERSION}"
    ./configure \
        --build="$gnuArch" \
        --enable-loadable-sqlite-extensions \
        --enable-shared \
        --with-system-expat \
        --with-system-ffi \
        --without-ensurepip \
        --enable-unicode=ucs4 \
        --prefix=/usr/local \
        LDFLAGS="-Wl,--rpath=/usr/local/lib"

    make -j "$(nproc)"

    EXTRA_CFLAGS="-DTHREAD_STACK_SIZE=0x100000" make install

    # Cleanup
    rm -Rf "/usr/src/python_${PYTHON_VERSION}"
    clean_pyc


done


# Install pip
cd /tmp
wget -O get-pip.py "https://bootstrap.pypa.io/get-pip.py"
for PYTHON_VERSION in $PYTHON_VERSIONS; do

    # Install pip

    python${PYTHON_VERSION%.*} get-pip.py \
        --disable-pip-version-check \
        --no-cache-dir \
        "pip==$PYTHON_PIP_VERSION"

    # Cleanup
    clean_pyc
done
