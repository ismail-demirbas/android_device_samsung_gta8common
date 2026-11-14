#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from gta8 device
$(call inherit-product, device/samsung/gta8/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_DEVICE := gta8
PRODUCT_NAME := lineage_gta8
PRODUCT_BRAND := samsung
PRODUCT_MODEL := SM-X205
PRODUCT_MANUFACTURER := samsung

TARGET_OTA_ASSERT_DEVICE := gta8,gta8tur

PRODUCT_GMS_CLIENTID_BASE := android-samsung-ss
