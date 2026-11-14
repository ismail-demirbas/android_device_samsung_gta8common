M=$(grep -i '^ro.product.vendor.model=' /vendor/build.prop | head -n1 | cut -d= -f2 | tr -d ' \r' | tr 'a-z' 'A-Z')
case "$M" in
  SM-X207) printf x207 > /tmp/gta8_model ;;
  SM-X205) printf x205 > /tmp/gta8_model ;;
  *) printf "" > /tmp/gta8_model ;;
esac
