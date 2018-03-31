#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/connie/robo_squad/src/squad"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/connie/robo_squad/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/connie/robo_squad/install/lib/python2.7/dist-packages:/home/connie/robo_squad/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/connie/robo_squad/build" \
    "/usr/bin/python" \
    "/home/connie/robo_squad/src/squad/setup.py" \
    build --build-base "/home/connie/robo_squad/build/squad" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/connie/robo_squad/install" --install-scripts="/home/connie/robo_squad/install/bin"
