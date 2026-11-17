if [ "$(cat /tmp/gta8_model)" = "x207" ]; then
  for f in /vendor/build.prop /vendor/odm/etc/build.prop; do
    [ -f "$f" ] && sed -i -e 's/SM-X205/SM-X207/g' "$f"
  done
  /system/bin/restorecon -R /vendor 2>/dev/null || restorecon -R /vendor 2>/dev/null
fi
