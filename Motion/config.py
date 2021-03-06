config = {
    'timeToSleepWhenNoMovement': 1,
    'timeToWaitWhenNoMovementBeforeSleep': 5,
    'frameDifferenceRatioForMovement': 1,
    'hand': {
        'hsv_min_blue': [0, 0, 0],
        'hsv_max_blue': [255, 255, 255],
        'hsv_dec_blue': [255, 55, 32],
        'hsv_inc_blue': [255, 255, 255],
        'timeToKeepSearchingHandWhenLostTracking': 1,
        'minimumHeight': 80,
        'maximumHeight': 350,
        'minimumWidth': 80,
        'maximumWidth': 320,
        'thumbsDetectMinimumHeightRatio': 0.12,
        'MaximumYDistanceBetweenDefectForPalmInHandRatio': 0.08,
        'MaximumXDistanceBetweenDefectForPalmInHandRatio': 0.2,
        'minimumMoveHandForSlide':  150,
        'maximumTimeHandForSlide': 0.5,
        'delayAfterHandSlide': 0.5
    }
}