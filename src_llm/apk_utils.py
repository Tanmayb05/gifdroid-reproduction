"""APK metadata extraction utilities."""
from __future__ import annotations

from pathlib import Path

import apkutils2


def extract_package_name(apk_path: Path) -> str:
    """Return the package name declared in the APK manifest."""
    apk = apkutils2.APK(str(apk_path))
    return apk.get_manifest().get("@package", "")


def extract_main_activity(apk_path: Path) -> str | None:
    """Return the main launcher activity name, or None if not found."""
    apk = apkutils2.APK(str(apk_path))
    manifest = apk.get_manifest()

    application = manifest.get("application", {})
    activities = application.get("activity", [])
    if isinstance(activities, dict):
        activities = [activities]

    for activity in activities:
        intent_filters = activity.get("intent-filter", [])
        if isinstance(intent_filters, dict):
            intent_filters = [intent_filters]
        for f in intent_filters:
            actions = f.get("action", [])
            if isinstance(actions, dict):
                actions = [actions]
            categories = f.get("category", [])
            if isinstance(categories, dict):
                categories = [categories]

            action_names = [a.get("@android:name", "") for a in actions]
            category_names = [c.get("@android:name", "") for c in categories]

            if (
                "android.intent.action.MAIN" in action_names
                and "android.intent.category.LAUNCHER" in category_names
            ):
                return activity.get("@android:name")

    return None
