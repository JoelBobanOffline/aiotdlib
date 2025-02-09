# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #

import typing

from .base_object import BaseObject
from .functions import *
from .types import *

if typing.TYPE_CHECKING:
    from aiotdlib.client import Client

ReturnType = typing.TypeVar('ReturnType', bound=BaseObject)


class API:
    """
    This class contains all TDJson API methods
    """

    class Types:
        # Types and Functions
        ANY = '*'
        ACCEPT_CALL = 'acceptCall'
        ACCEPT_TERMS_OF_SERVICE = 'acceptTermsOfService'
        ACCOUNT_TTL = 'accountTtl'
        ADD_CHAT_MEMBER = 'addChatMember'
        ADD_CHAT_MEMBERS = 'addChatMembers'
        ADD_CHAT_TO_LIST = 'addChatToList'
        ADD_CONTACT = 'addContact'
        ADD_CUSTOM_SERVER_LANGUAGE_PACK = 'addCustomServerLanguagePack'
        ADD_FAVORITE_STICKER = 'addFavoriteSticker'
        ADD_FILE_TO_DOWNLOADS = 'addFileToDownloads'
        ADD_LOCAL_MESSAGE = 'addLocalMessage'
        ADD_LOG_MESSAGE = 'addLogMessage'
        ADD_NETWORK_STATISTICS = 'addNetworkStatistics'
        ADD_PROXY = 'addProxy'
        ADD_RECENT_STICKER = 'addRecentSticker'
        ADD_RECENTLY_FOUND_CHAT = 'addRecentlyFoundChat'
        ADD_SAVED_ANIMATION = 'addSavedAnimation'
        ADD_SAVED_NOTIFICATION_SOUND = 'addSavedNotificationSound'
        ADD_STICKER_TO_SET = 'addStickerToSet'
        ADDED_REACTION = 'addedReaction'
        ADDED_REACTIONS = 'addedReactions'
        ADDRESS = 'address'
        ANIMATED_CHAT_PHOTO = 'animatedChatPhoto'
        ANIMATED_EMOJI = 'animatedEmoji'
        ANIMATION = 'animation'
        ANIMATIONS = 'animations'
        ANSWER_CALLBACK_QUERY = 'answerCallbackQuery'
        ANSWER_CUSTOM_QUERY = 'answerCustomQuery'
        ANSWER_INLINE_QUERY = 'answerInlineQuery'
        ANSWER_PRE_CHECKOUT_QUERY = 'answerPreCheckoutQuery'
        ANSWER_SHIPPING_QUERY = 'answerShippingQuery'
        ANSWER_WEB_APP_QUERY = 'answerWebAppQuery'
        ATTACHMENT_MENU_BOT = 'attachmentMenuBot'
        ATTACHMENT_MENU_BOT_COLOR = 'attachmentMenuBotColor'
        AUDIO = 'audio'
        AUTHENTICATION_CODE_INFO = 'authenticationCodeInfo'
        AUTHENTICATION_CODE_TYPE = 'authenticationCodeType'
        AUTHENTICATION_CODE_TYPE_CALL = 'authenticationCodeTypeCall'
        AUTHENTICATION_CODE_TYPE_FLASH_CALL = 'authenticationCodeTypeFlashCall'
        AUTHENTICATION_CODE_TYPE_MISSED_CALL = 'authenticationCodeTypeMissedCall'
        AUTHENTICATION_CODE_TYPE_SMS = 'authenticationCodeTypeSms'
        AUTHENTICATION_CODE_TYPE_TELEGRAM_MESSAGE = 'authenticationCodeTypeTelegramMessage'
        AUTHORIZATION_STATE = 'authorizationState'
        AUTHORIZATION_STATE_CLOSED = 'authorizationStateClosed'
        AUTHORIZATION_STATE_CLOSING = 'authorizationStateClosing'
        AUTHORIZATION_STATE_LOGGING_OUT = 'authorizationStateLoggingOut'
        AUTHORIZATION_STATE_READY = 'authorizationStateReady'
        AUTHORIZATION_STATE_WAIT_CODE = 'authorizationStateWaitCode'
        AUTHORIZATION_STATE_WAIT_ENCRYPTION_KEY = 'authorizationStateWaitEncryptionKey'
        AUTHORIZATION_STATE_WAIT_OTHER_DEVICE_CONFIRMATION = 'authorizationStateWaitOtherDeviceConfirmation'
        AUTHORIZATION_STATE_WAIT_PASSWORD = 'authorizationStateWaitPassword'
        AUTHORIZATION_STATE_WAIT_PHONE_NUMBER = 'authorizationStateWaitPhoneNumber'
        AUTHORIZATION_STATE_WAIT_REGISTRATION = 'authorizationStateWaitRegistration'
        AUTHORIZATION_STATE_WAIT_TDLIB_PARAMETERS = 'authorizationStateWaitTdlibParameters'
        AUTO_DOWNLOAD_SETTINGS = 'autoDownloadSettings'
        AUTO_DOWNLOAD_SETTINGS_PRESETS = 'autoDownloadSettingsPresets'
        AVAILABLE_REACTIONS = 'availableReactions'
        BACKGROUND = 'background'
        BACKGROUND_FILL = 'backgroundFill'
        BACKGROUND_FILL_FREEFORM_GRADIENT = 'backgroundFillFreeformGradient'
        BACKGROUND_FILL_GRADIENT = 'backgroundFillGradient'
        BACKGROUND_FILL_SOLID = 'backgroundFillSolid'
        BACKGROUND_TYPE = 'backgroundType'
        BACKGROUND_TYPE_FILL = 'backgroundTypeFill'
        BACKGROUND_TYPE_PATTERN = 'backgroundTypePattern'
        BACKGROUND_TYPE_WALLPAPER = 'backgroundTypeWallpaper'
        BACKGROUNDS = 'backgrounds'
        BAN_CHAT_MEMBER = 'banChatMember'
        BANK_CARD_ACTION_OPEN_URL = 'bankCardActionOpenUrl'
        BANK_CARD_INFO = 'bankCardInfo'
        BASIC_GROUP = 'basicGroup'
        BASIC_GROUP_FULL_INFO = 'basicGroupFullInfo'
        BLOCK_MESSAGE_SENDER_FROM_REPLIES = 'blockMessageSenderFromReplies'
        BOT_COMMAND = 'botCommand'
        BOT_COMMAND_SCOPE = 'botCommandScope'
        BOT_COMMAND_SCOPE_ALL_CHAT_ADMINISTRATORS = 'botCommandScopeAllChatAdministrators'
        BOT_COMMAND_SCOPE_ALL_GROUP_CHATS = 'botCommandScopeAllGroupChats'
        BOT_COMMAND_SCOPE_ALL_PRIVATE_CHATS = 'botCommandScopeAllPrivateChats'
        BOT_COMMAND_SCOPE_CHAT = 'botCommandScopeChat'
        BOT_COMMAND_SCOPE_CHAT_ADMINISTRATORS = 'botCommandScopeChatAdministrators'
        BOT_COMMAND_SCOPE_CHAT_MEMBER = 'botCommandScopeChatMember'
        BOT_COMMAND_SCOPE_DEFAULT = 'botCommandScopeDefault'
        BOT_COMMANDS = 'botCommands'
        BOT_INFO = 'botInfo'
        BOT_MENU_BUTTON = 'botMenuButton'
        CALL = 'call'
        CALL_DISCARD_REASON = 'callDiscardReason'
        CALL_DISCARD_REASON_DECLINED = 'callDiscardReasonDeclined'
        CALL_DISCARD_REASON_DISCONNECTED = 'callDiscardReasonDisconnected'
        CALL_DISCARD_REASON_EMPTY = 'callDiscardReasonEmpty'
        CALL_DISCARD_REASON_HUNG_UP = 'callDiscardReasonHungUp'
        CALL_DISCARD_REASON_MISSED = 'callDiscardReasonMissed'
        CALL_ID = 'callId'
        CALL_PROBLEM = 'callProblem'
        CALL_PROBLEM_DISTORTED_SPEECH = 'callProblemDistortedSpeech'
        CALL_PROBLEM_DISTORTED_VIDEO = 'callProblemDistortedVideo'
        CALL_PROBLEM_DROPPED = 'callProblemDropped'
        CALL_PROBLEM_ECHO = 'callProblemEcho'
        CALL_PROBLEM_INTERRUPTIONS = 'callProblemInterruptions'
        CALL_PROBLEM_NOISE = 'callProblemNoise'
        CALL_PROBLEM_PIXELATED_VIDEO = 'callProblemPixelatedVideo'
        CALL_PROBLEM_SILENT_LOCAL = 'callProblemSilentLocal'
        CALL_PROBLEM_SILENT_REMOTE = 'callProblemSilentRemote'
        CALL_PROTOCOL = 'callProtocol'
        CALL_SERVER = 'callServer'
        CALL_SERVER_TYPE = 'callServerType'
        CALL_SERVER_TYPE_TELEGRAM_REFLECTOR = 'callServerTypeTelegramReflector'
        CALL_SERVER_TYPE_WEBRTC = 'callServerTypeWebrtc'
        CALL_STATE = 'callState'
        CALL_STATE_DISCARDED = 'callStateDiscarded'
        CALL_STATE_ERROR = 'callStateError'
        CALL_STATE_EXCHANGING_KEYS = 'callStateExchangingKeys'
        CALL_STATE_HANGING_UP = 'callStateHangingUp'
        CALL_STATE_PENDING = 'callStatePending'
        CALL_STATE_READY = 'callStateReady'
        CALLBACK_QUERY_ANSWER = 'callbackQueryAnswer'
        CALLBACK_QUERY_PAYLOAD = 'callbackQueryPayload'
        CALLBACK_QUERY_PAYLOAD_DATA = 'callbackQueryPayloadData'
        CALLBACK_QUERY_PAYLOAD_DATA_WITH_PASSWORD = 'callbackQueryPayloadDataWithPassword'
        CALLBACK_QUERY_PAYLOAD_GAME = 'callbackQueryPayloadGame'
        CAN_TRANSFER_OWNERSHIP = 'canTransferOwnership'
        CAN_TRANSFER_OWNERSHIP_RESULT = 'canTransferOwnershipResult'
        CAN_TRANSFER_OWNERSHIP_RESULT_OK = 'canTransferOwnershipResultOk'
        CAN_TRANSFER_OWNERSHIP_RESULT_PASSWORD_NEEDED = 'canTransferOwnershipResultPasswordNeeded'
        CAN_TRANSFER_OWNERSHIP_RESULT_PASSWORD_TOO_FRESH = 'canTransferOwnershipResultPasswordTooFresh'
        CAN_TRANSFER_OWNERSHIP_RESULT_SESSION_TOO_FRESH = 'canTransferOwnershipResultSessionTooFresh'
        CANCEL_DOWNLOAD_FILE = 'cancelDownloadFile'
        CANCEL_PASSWORD_RESET = 'cancelPasswordReset'
        CANCEL_UPLOAD_FILE = 'cancelUploadFile'
        CHANGE_IMPORTED_CONTACTS = 'changeImportedContacts'
        CHANGE_PHONE_NUMBER = 'changePhoneNumber'
        CHANGE_STICKER_SET = 'changeStickerSet'
        CHAT = 'chat'
        CHAT_ACTION = 'chatAction'
        CHAT_ACTION_CANCEL = 'chatActionCancel'
        CHAT_ACTION_CHOOSING_CONTACT = 'chatActionChoosingContact'
        CHAT_ACTION_CHOOSING_LOCATION = 'chatActionChoosingLocation'
        CHAT_ACTION_CHOOSING_STICKER = 'chatActionChoosingSticker'
        CHAT_ACTION_RECORDING_VIDEO = 'chatActionRecordingVideo'
        CHAT_ACTION_RECORDING_VIDEO_NOTE = 'chatActionRecordingVideoNote'
        CHAT_ACTION_RECORDING_VOICE_NOTE = 'chatActionRecordingVoiceNote'
        CHAT_ACTION_START_PLAYING_GAME = 'chatActionStartPlayingGame'
        CHAT_ACTION_TYPING = 'chatActionTyping'
        CHAT_ACTION_UPLOADING_DOCUMENT = 'chatActionUploadingDocument'
        CHAT_ACTION_UPLOADING_PHOTO = 'chatActionUploadingPhoto'
        CHAT_ACTION_UPLOADING_VIDEO = 'chatActionUploadingVideo'
        CHAT_ACTION_UPLOADING_VIDEO_NOTE = 'chatActionUploadingVideoNote'
        CHAT_ACTION_UPLOADING_VOICE_NOTE = 'chatActionUploadingVoiceNote'
        CHAT_ACTION_WATCHING_ANIMATIONS = 'chatActionWatchingAnimations'
        CHAT_ACTION_BAR = 'chatActionBar'
        CHAT_ACTION_BAR_ADD_CONTACT = 'chatActionBarAddContact'
        CHAT_ACTION_BAR_INVITE_MEMBERS = 'chatActionBarInviteMembers'
        CHAT_ACTION_BAR_JOIN_REQUEST = 'chatActionBarJoinRequest'
        CHAT_ACTION_BAR_REPORT_ADD_BLOCK = 'chatActionBarReportAddBlock'
        CHAT_ACTION_BAR_REPORT_SPAM = 'chatActionBarReportSpam'
        CHAT_ACTION_BAR_REPORT_UNRELATED_LOCATION = 'chatActionBarReportUnrelatedLocation'
        CHAT_ACTION_BAR_SHARE_PHONE_NUMBER = 'chatActionBarSharePhoneNumber'
        CHAT_ADMINISTRATOR = 'chatAdministrator'
        CHAT_ADMINISTRATOR_RIGHTS = 'chatAdministratorRights'
        CHAT_ADMINISTRATORS = 'chatAdministrators'
        CHAT_EVENT = 'chatEvent'
        CHAT_EVENT_ACTION = 'chatEventAction'
        CHAT_EVENT_AVAILABLE_REACTIONS_CHANGED = 'chatEventAvailableReactionsChanged'
        CHAT_EVENT_DESCRIPTION_CHANGED = 'chatEventDescriptionChanged'
        CHAT_EVENT_HAS_PROTECTED_CONTENT_TOGGLED = 'chatEventHasProtectedContentToggled'
        CHAT_EVENT_INVITE_LINK_DELETED = 'chatEventInviteLinkDeleted'
        CHAT_EVENT_INVITE_LINK_EDITED = 'chatEventInviteLinkEdited'
        CHAT_EVENT_INVITE_LINK_REVOKED = 'chatEventInviteLinkRevoked'
        CHAT_EVENT_INVITES_TOGGLED = 'chatEventInvitesToggled'
        CHAT_EVENT_IS_ALL_HISTORY_AVAILABLE_TOGGLED = 'chatEventIsAllHistoryAvailableToggled'
        CHAT_EVENT_LINKED_CHAT_CHANGED = 'chatEventLinkedChatChanged'
        CHAT_EVENT_LOCATION_CHANGED = 'chatEventLocationChanged'
        CHAT_EVENT_MEMBER_INVITED = 'chatEventMemberInvited'
        CHAT_EVENT_MEMBER_JOINED = 'chatEventMemberJoined'
        CHAT_EVENT_MEMBER_JOINED_BY_INVITE_LINK = 'chatEventMemberJoinedByInviteLink'
        CHAT_EVENT_MEMBER_JOINED_BY_REQUEST = 'chatEventMemberJoinedByRequest'
        CHAT_EVENT_MEMBER_LEFT = 'chatEventMemberLeft'
        CHAT_EVENT_MEMBER_PROMOTED = 'chatEventMemberPromoted'
        CHAT_EVENT_MEMBER_RESTRICTED = 'chatEventMemberRestricted'
        CHAT_EVENT_MESSAGE_DELETED = 'chatEventMessageDeleted'
        CHAT_EVENT_MESSAGE_EDITED = 'chatEventMessageEdited'
        CHAT_EVENT_MESSAGE_PINNED = 'chatEventMessagePinned'
        CHAT_EVENT_MESSAGE_TTL_CHANGED = 'chatEventMessageTtlChanged'
        CHAT_EVENT_MESSAGE_UNPINNED = 'chatEventMessageUnpinned'
        CHAT_EVENT_PERMISSIONS_CHANGED = 'chatEventPermissionsChanged'
        CHAT_EVENT_PHOTO_CHANGED = 'chatEventPhotoChanged'
        CHAT_EVENT_POLL_STOPPED = 'chatEventPollStopped'
        CHAT_EVENT_SIGN_MESSAGES_TOGGLED = 'chatEventSignMessagesToggled'
        CHAT_EVENT_SLOW_MODE_DELAY_CHANGED = 'chatEventSlowModeDelayChanged'
        CHAT_EVENT_STICKER_SET_CHANGED = 'chatEventStickerSetChanged'
        CHAT_EVENT_TITLE_CHANGED = 'chatEventTitleChanged'
        CHAT_EVENT_USERNAME_CHANGED = 'chatEventUsernameChanged'
        CHAT_EVENT_VIDEO_CHAT_CREATED = 'chatEventVideoChatCreated'
        CHAT_EVENT_VIDEO_CHAT_ENDED = 'chatEventVideoChatEnded'
        CHAT_EVENT_VIDEO_CHAT_MUTE_NEW_PARTICIPANTS_TOGGLED = 'chatEventVideoChatMuteNewParticipantsToggled'
        CHAT_EVENT_VIDEO_CHAT_PARTICIPANT_IS_MUTED_TOGGLED = 'chatEventVideoChatParticipantIsMutedToggled'
        CHAT_EVENT_VIDEO_CHAT_PARTICIPANT_VOLUME_LEVEL_CHANGED = 'chatEventVideoChatParticipantVolumeLevelChanged'
        CHAT_EVENT_LOG_FILTERS = 'chatEventLogFilters'
        CHAT_EVENTS = 'chatEvents'
        CHAT_FILTER = 'chatFilter'
        CHAT_FILTER_INFO = 'chatFilterInfo'
        CHAT_INVITE_LINK = 'chatInviteLink'
        CHAT_INVITE_LINK_COUNT = 'chatInviteLinkCount'
        CHAT_INVITE_LINK_COUNTS = 'chatInviteLinkCounts'
        CHAT_INVITE_LINK_INFO = 'chatInviteLinkInfo'
        CHAT_INVITE_LINK_MEMBER = 'chatInviteLinkMember'
        CHAT_INVITE_LINK_MEMBERS = 'chatInviteLinkMembers'
        CHAT_INVITE_LINKS = 'chatInviteLinks'
        CHAT_JOIN_REQUEST = 'chatJoinRequest'
        CHAT_JOIN_REQUESTS = 'chatJoinRequests'
        CHAT_JOIN_REQUESTS_INFO = 'chatJoinRequestsInfo'
        CHAT_LIST = 'chatList'
        CHAT_LIST_ARCHIVE = 'chatListArchive'
        CHAT_LIST_FILTER = 'chatListFilter'
        CHAT_LIST_MAIN = 'chatListMain'
        CHAT_LISTS = 'chatLists'
        CHAT_LOCATION = 'chatLocation'
        CHAT_MEMBER = 'chatMember'
        CHAT_MEMBER_STATUS = 'chatMemberStatus'
        CHAT_MEMBER_STATUS_ADMINISTRATOR = 'chatMemberStatusAdministrator'
        CHAT_MEMBER_STATUS_BANNED = 'chatMemberStatusBanned'
        CHAT_MEMBER_STATUS_CREATOR = 'chatMemberStatusCreator'
        CHAT_MEMBER_STATUS_LEFT = 'chatMemberStatusLeft'
        CHAT_MEMBER_STATUS_MEMBER = 'chatMemberStatusMember'
        CHAT_MEMBER_STATUS_RESTRICTED = 'chatMemberStatusRestricted'
        CHAT_MEMBERS = 'chatMembers'
        CHAT_MEMBERS_FILTER = 'chatMembersFilter'
        CHAT_MEMBERS_FILTER_ADMINISTRATORS = 'chatMembersFilterAdministrators'
        CHAT_MEMBERS_FILTER_BANNED = 'chatMembersFilterBanned'
        CHAT_MEMBERS_FILTER_BOTS = 'chatMembersFilterBots'
        CHAT_MEMBERS_FILTER_CONTACTS = 'chatMembersFilterContacts'
        CHAT_MEMBERS_FILTER_MEMBERS = 'chatMembersFilterMembers'
        CHAT_MEMBERS_FILTER_MENTION = 'chatMembersFilterMention'
        CHAT_MEMBERS_FILTER_RESTRICTED = 'chatMembersFilterRestricted'
        CHAT_NEARBY = 'chatNearby'
        CHAT_NOTIFICATION_SETTINGS = 'chatNotificationSettings'
        CHAT_PERMISSIONS = 'chatPermissions'
        CHAT_PHOTO = 'chatPhoto'
        CHAT_PHOTO_INFO = 'chatPhotoInfo'
        CHAT_PHOTOS = 'chatPhotos'
        CHAT_POSITION = 'chatPosition'
        CHAT_REPORT_REASON = 'chatReportReason'
        CHAT_REPORT_REASON_CHILD_ABUSE = 'chatReportReasonChildAbuse'
        CHAT_REPORT_REASON_COPYRIGHT = 'chatReportReasonCopyright'
        CHAT_REPORT_REASON_CUSTOM = 'chatReportReasonCustom'
        CHAT_REPORT_REASON_FAKE = 'chatReportReasonFake'
        CHAT_REPORT_REASON_ILLEGAL_DRUGS = 'chatReportReasonIllegalDrugs'
        CHAT_REPORT_REASON_PERSONAL_DETAILS = 'chatReportReasonPersonalDetails'
        CHAT_REPORT_REASON_PORNOGRAPHY = 'chatReportReasonPornography'
        CHAT_REPORT_REASON_SPAM = 'chatReportReasonSpam'
        CHAT_REPORT_REASON_UNRELATED_LOCATION = 'chatReportReasonUnrelatedLocation'
        CHAT_REPORT_REASON_VIOLENCE = 'chatReportReasonViolence'
        CHAT_SOURCE = 'chatSource'
        CHAT_SOURCE_MTPROTO_PROXY = 'chatSourceMtprotoProxy'
        CHAT_SOURCE_PUBLIC_SERVICE_ANNOUNCEMENT = 'chatSourcePublicServiceAnnouncement'
        CHAT_STATISTICS = 'chatStatistics'
        CHAT_STATISTICS_CHANNEL = 'chatStatisticsChannel'
        CHAT_STATISTICS_SUPERGROUP = 'chatStatisticsSupergroup'
        CHAT_STATISTICS_ADMINISTRATOR_ACTIONS_INFO = 'chatStatisticsAdministratorActionsInfo'
        CHAT_STATISTICS_INVITER_INFO = 'chatStatisticsInviterInfo'
        CHAT_STATISTICS_MESSAGE_INTERACTION_INFO = 'chatStatisticsMessageInteractionInfo'
        CHAT_STATISTICS_MESSAGE_SENDER_INFO = 'chatStatisticsMessageSenderInfo'
        CHAT_THEME = 'chatTheme'
        CHAT_TYPE = 'chatType'
        CHAT_TYPE_BASIC_GROUP = 'chatTypeBasicGroup'
        CHAT_TYPE_PRIVATE = 'chatTypePrivate'
        CHAT_TYPE_SECRET = 'chatTypeSecret'
        CHAT_TYPE_SUPERGROUP = 'chatTypeSupergroup'
        CHATS = 'chats'
        CHATS_NEARBY = 'chatsNearby'
        CHECK_AUTHENTICATION_BOT_TOKEN = 'checkAuthenticationBotToken'
        CHECK_AUTHENTICATION_CODE = 'checkAuthenticationCode'
        CHECK_AUTHENTICATION_PASSWORD = 'checkAuthenticationPassword'
        CHECK_AUTHENTICATION_PASSWORD_RECOVERY_CODE = 'checkAuthenticationPasswordRecoveryCode'
        CHECK_CHANGE_PHONE_NUMBER_CODE = 'checkChangePhoneNumberCode'
        CHECK_CHAT_INVITE_LINK = 'checkChatInviteLink'
        CHECK_CHAT_USERNAME = 'checkChatUsername'
        CHECK_CHAT_USERNAME_RESULT = 'checkChatUsernameResult'
        CHECK_CHAT_USERNAME_RESULT_OK = 'checkChatUsernameResultOk'
        CHECK_CHAT_USERNAME_RESULT_PUBLIC_CHATS_TOO_MUCH = 'checkChatUsernameResultPublicChatsTooMuch'
        CHECK_CHAT_USERNAME_RESULT_PUBLIC_GROUPS_UNAVAILABLE = 'checkChatUsernameResultPublicGroupsUnavailable'
        CHECK_CHAT_USERNAME_RESULT_USERNAME_INVALID = 'checkChatUsernameResultUsernameInvalid'
        CHECK_CHAT_USERNAME_RESULT_USERNAME_OCCUPIED = 'checkChatUsernameResultUsernameOccupied'
        CHECK_CREATED_PUBLIC_CHATS_LIMIT = 'checkCreatedPublicChatsLimit'
        CHECK_DATABASE_ENCRYPTION_KEY = 'checkDatabaseEncryptionKey'
        CHECK_EMAIL_ADDRESS_VERIFICATION_CODE = 'checkEmailAddressVerificationCode'
        CHECK_PASSWORD_RECOVERY_CODE = 'checkPasswordRecoveryCode'
        CHECK_PHONE_NUMBER_CONFIRMATION_CODE = 'checkPhoneNumberConfirmationCode'
        CHECK_PHONE_NUMBER_VERIFICATION_CODE = 'checkPhoneNumberVerificationCode'
        CHECK_RECOVERY_EMAIL_ADDRESS_CODE = 'checkRecoveryEmailAddressCode'
        CHECK_STICKER_SET_NAME = 'checkStickerSetName'
        CHECK_STICKER_SET_NAME_RESULT = 'checkStickerSetNameResult'
        CHECK_STICKER_SET_NAME_RESULT_NAME_INVALID = 'checkStickerSetNameResultNameInvalid'
        CHECK_STICKER_SET_NAME_RESULT_NAME_OCCUPIED = 'checkStickerSetNameResultNameOccupied'
        CHECK_STICKER_SET_NAME_RESULT_OK = 'checkStickerSetNameResultOk'
        CLEAN_FILE_NAME = 'cleanFileName'
        CLEAR_ALL_DRAFT_MESSAGES = 'clearAllDraftMessages'
        CLEAR_IMPORTED_CONTACTS = 'clearImportedContacts'
        CLEAR_RECENT_STICKERS = 'clearRecentStickers'
        CLEAR_RECENTLY_FOUND_CHATS = 'clearRecentlyFoundChats'
        CLICK_ANIMATED_EMOJI_MESSAGE = 'clickAnimatedEmojiMessage'
        CLOSE = 'close'
        CLOSE_CHAT = 'closeChat'
        CLOSE_SECRET_CHAT = 'closeSecretChat'
        CLOSE_WEB_APP = 'closeWebApp'
        CLOSED_VECTOR_PATH = 'closedVectorPath'
        CONFIRM_QR_CODE_AUTHENTICATION = 'confirmQrCodeAuthentication'
        CONNECTED_WEBSITE = 'connectedWebsite'
        CONNECTED_WEBSITES = 'connectedWebsites'
        CONNECTION_STATE = 'connectionState'
        CONNECTION_STATE_CONNECTING = 'connectionStateConnecting'
        CONNECTION_STATE_CONNECTING_TO_PROXY = 'connectionStateConnectingToProxy'
        CONNECTION_STATE_READY = 'connectionStateReady'
        CONNECTION_STATE_UPDATING = 'connectionStateUpdating'
        CONNECTION_STATE_WAITING_FOR_NETWORK = 'connectionStateWaitingForNetwork'
        CONTACT = 'contact'
        COUNT = 'count'
        COUNTRIES = 'countries'
        COUNTRY_INFO = 'countryInfo'
        CREATE_BASIC_GROUP_CHAT = 'createBasicGroupChat'
        CREATE_CALL = 'createCall'
        CREATE_CHAT_FILTER = 'createChatFilter'
        CREATE_CHAT_INVITE_LINK = 'createChatInviteLink'
        CREATE_NEW_BASIC_GROUP_CHAT = 'createNewBasicGroupChat'
        CREATE_NEW_SECRET_CHAT = 'createNewSecretChat'
        CREATE_NEW_STICKER_SET = 'createNewStickerSet'
        CREATE_NEW_SUPERGROUP_CHAT = 'createNewSupergroupChat'
        CREATE_PRIVATE_CHAT = 'createPrivateChat'
        CREATE_SECRET_CHAT = 'createSecretChat'
        CREATE_SUPERGROUP_CHAT = 'createSupergroupChat'
        CREATE_TEMPORARY_PASSWORD = 'createTemporaryPassword'
        CREATE_VIDEO_CHAT = 'createVideoChat'
        CUSTOM_REQUEST_RESULT = 'customRequestResult'
        DATABASE_STATISTICS = 'databaseStatistics'
        DATE = 'date'
        DATE_RANGE = 'dateRange'
        DATED_FILE = 'datedFile'
        DEEP_LINK_INFO = 'deepLinkInfo'
        DELETE_ACCOUNT = 'deleteAccount'
        DELETE_ALL_CALL_MESSAGES = 'deleteAllCallMessages'
        DELETE_ALL_REVOKED_CHAT_INVITE_LINKS = 'deleteAllRevokedChatInviteLinks'
        DELETE_CHAT = 'deleteChat'
        DELETE_CHAT_FILTER = 'deleteChatFilter'
        DELETE_CHAT_HISTORY = 'deleteChatHistory'
        DELETE_CHAT_MESSAGES_BY_DATE = 'deleteChatMessagesByDate'
        DELETE_CHAT_MESSAGES_BY_SENDER = 'deleteChatMessagesBySender'
        DELETE_CHAT_REPLY_MARKUP = 'deleteChatReplyMarkup'
        DELETE_COMMANDS = 'deleteCommands'
        DELETE_FILE = 'deleteFile'
        DELETE_LANGUAGE_PACK = 'deleteLanguagePack'
        DELETE_MESSAGES = 'deleteMessages'
        DELETE_PASSPORT_ELEMENT = 'deletePassportElement'
        DELETE_PROFILE_PHOTO = 'deleteProfilePhoto'
        DELETE_REVOKED_CHAT_INVITE_LINK = 'deleteRevokedChatInviteLink'
        DELETE_SAVED_CREDENTIALS = 'deleteSavedCredentials'
        DELETE_SAVED_ORDER_INFO = 'deleteSavedOrderInfo'
        DESTROY = 'destroy'
        DEVICE_TOKEN = 'deviceToken'
        DEVICE_TOKEN_APPLE_PUSH = 'deviceTokenApplePush'
        DEVICE_TOKEN_APPLE_PUSH_VO_IP = 'deviceTokenApplePushVoIP'
        DEVICE_TOKEN_BLACK_BERRY_PUSH = 'deviceTokenBlackBerryPush'
        DEVICE_TOKEN_FIREBASE_CLOUD_MESSAGING = 'deviceTokenFirebaseCloudMessaging'
        DEVICE_TOKEN_MICROSOFT_PUSH = 'deviceTokenMicrosoftPush'
        DEVICE_TOKEN_MICROSOFT_PUSH_VO_IP = 'deviceTokenMicrosoftPushVoIP'
        DEVICE_TOKEN_SIMPLE_PUSH = 'deviceTokenSimplePush'
        DEVICE_TOKEN_TIZEN_PUSH = 'deviceTokenTizenPush'
        DEVICE_TOKEN_UBUNTU_PUSH = 'deviceTokenUbuntuPush'
        DEVICE_TOKEN_WEB_PUSH = 'deviceTokenWebPush'
        DEVICE_TOKEN_WINDOWS_PUSH = 'deviceTokenWindowsPush'
        DICE_STICKERS = 'diceStickers'
        DICE_STICKERS_REGULAR = 'diceStickersRegular'
        DICE_STICKERS_SLOT_MACHINE = 'diceStickersSlotMachine'
        DISABLE_PROXY = 'disableProxy'
        DISCARD_CALL = 'discardCall'
        DISCONNECT_ALL_WEBSITES = 'disconnectAllWebsites'
        DISCONNECT_WEBSITE = 'disconnectWebsite'
        DOCUMENT = 'document'
        DOWNLOAD_FILE = 'downloadFile'
        DOWNLOADED_FILE_COUNTS = 'downloadedFileCounts'
        DRAFT_MESSAGE = 'draftMessage'
        EDIT_CHAT_FILTER = 'editChatFilter'
        EDIT_CHAT_INVITE_LINK = 'editChatInviteLink'
        EDIT_CUSTOM_LANGUAGE_PACK_INFO = 'editCustomLanguagePackInfo'
        EDIT_INLINE_MESSAGE_CAPTION = 'editInlineMessageCaption'
        EDIT_INLINE_MESSAGE_LIVE_LOCATION = 'editInlineMessageLiveLocation'
        EDIT_INLINE_MESSAGE_MEDIA = 'editInlineMessageMedia'
        EDIT_INLINE_MESSAGE_REPLY_MARKUP = 'editInlineMessageReplyMarkup'
        EDIT_INLINE_MESSAGE_TEXT = 'editInlineMessageText'
        EDIT_MESSAGE_CAPTION = 'editMessageCaption'
        EDIT_MESSAGE_LIVE_LOCATION = 'editMessageLiveLocation'
        EDIT_MESSAGE_MEDIA = 'editMessageMedia'
        EDIT_MESSAGE_REPLY_MARKUP = 'editMessageReplyMarkup'
        EDIT_MESSAGE_SCHEDULING_STATE = 'editMessageSchedulingState'
        EDIT_MESSAGE_TEXT = 'editMessageText'
        EDIT_PROXY = 'editProxy'
        EMAIL_ADDRESS_AUTHENTICATION_CODE_INFO = 'emailAddressAuthenticationCodeInfo'
        EMOJIS = 'emojis'
        ENABLE_PROXY = 'enableProxy'
        ENCRYPTED_CREDENTIALS = 'encryptedCredentials'
        ENCRYPTED_PASSPORT_ELEMENT = 'encryptedPassportElement'
        END_GROUP_CALL = 'endGroupCall'
        END_GROUP_CALL_RECORDING = 'endGroupCallRecording'
        END_GROUP_CALL_SCREEN_SHARING = 'endGroupCallScreenSharing'
        ERROR = 'error'
        FILE = 'file'
        FILE_DOWNLOAD = 'fileDownload'
        FILE_PART = 'filePart'
        FILE_TYPE = 'fileType'
        FILE_TYPE_ANIMATION = 'fileTypeAnimation'
        FILE_TYPE_AUDIO = 'fileTypeAudio'
        FILE_TYPE_DOCUMENT = 'fileTypeDocument'
        FILE_TYPE_NONE = 'fileTypeNone'
        FILE_TYPE_NOTIFICATION_SOUND = 'fileTypeNotificationSound'
        FILE_TYPE_PHOTO = 'fileTypePhoto'
        FILE_TYPE_PROFILE_PHOTO = 'fileTypeProfilePhoto'
        FILE_TYPE_SECRET = 'fileTypeSecret'
        FILE_TYPE_SECRET_THUMBNAIL = 'fileTypeSecretThumbnail'
        FILE_TYPE_SECURE = 'fileTypeSecure'
        FILE_TYPE_STICKER = 'fileTypeSticker'
        FILE_TYPE_THUMBNAIL = 'fileTypeThumbnail'
        FILE_TYPE_UNKNOWN = 'fileTypeUnknown'
        FILE_TYPE_VIDEO = 'fileTypeVideo'
        FILE_TYPE_VIDEO_NOTE = 'fileTypeVideoNote'
        FILE_TYPE_VOICE_NOTE = 'fileTypeVoiceNote'
        FILE_TYPE_WALLPAPER = 'fileTypeWallpaper'
        FINISH_FILE_GENERATION = 'finishFileGeneration'
        FORMATTED_TEXT = 'formattedText'
        FORWARD_MESSAGES = 'forwardMessages'
        FOUND_FILE_DOWNLOADS = 'foundFileDownloads'
        FOUND_MESSAGES = 'foundMessages'
        GAME = 'game'
        GAME_HIGH_SCORE = 'gameHighScore'
        GAME_HIGH_SCORES = 'gameHighScores'
        GET_ACCOUNT_TTL = 'getAccountTtl'
        GET_ACTIVE_LIVE_LOCATION_MESSAGES = 'getActiveLiveLocationMessages'
        GET_ACTIVE_SESSIONS = 'getActiveSessions'
        GET_ALL_PASSPORT_ELEMENTS = 'getAllPassportElements'
        GET_ANIMATED_EMOJI = 'getAnimatedEmoji'
        GET_APPLICATION_CONFIG = 'getApplicationConfig'
        GET_APPLICATION_DOWNLOAD_LINK = 'getApplicationDownloadLink'
        GET_ARCHIVED_STICKER_SETS = 'getArchivedStickerSets'
        GET_ATTACHED_STICKER_SETS = 'getAttachedStickerSets'
        GET_ATTACHMENT_MENU_BOT = 'getAttachmentMenuBot'
        GET_AUTHORIZATION_STATE = 'getAuthorizationState'
        GET_AUTO_DOWNLOAD_SETTINGS_PRESETS = 'getAutoDownloadSettingsPresets'
        GET_BACKGROUND_URL = 'getBackgroundUrl'
        GET_BACKGROUNDS = 'getBackgrounds'
        GET_BANK_CARD_INFO = 'getBankCardInfo'
        GET_BASIC_GROUP = 'getBasicGroup'
        GET_BASIC_GROUP_FULL_INFO = 'getBasicGroupFullInfo'
        GET_BLOCKED_MESSAGE_SENDERS = 'getBlockedMessageSenders'
        GET_CALLBACK_QUERY_ANSWER = 'getCallbackQueryAnswer'
        GET_CALLBACK_QUERY_MESSAGE = 'getCallbackQueryMessage'
        GET_CHAT = 'getChat'
        GET_CHAT_ADMINISTRATORS = 'getChatAdministrators'
        GET_CHAT_AVAILABLE_MESSAGE_SENDERS = 'getChatAvailableMessageSenders'
        GET_CHAT_EVENT_LOG = 'getChatEventLog'
        GET_CHAT_FILTER = 'getChatFilter'
        GET_CHAT_FILTER_DEFAULT_ICON_NAME = 'getChatFilterDefaultIconName'
        GET_CHAT_HISTORY = 'getChatHistory'
        GET_CHAT_INVITE_LINK = 'getChatInviteLink'
        GET_CHAT_INVITE_LINK_COUNTS = 'getChatInviteLinkCounts'
        GET_CHAT_INVITE_LINK_MEMBERS = 'getChatInviteLinkMembers'
        GET_CHAT_INVITE_LINKS = 'getChatInviteLinks'
        GET_CHAT_JOIN_REQUESTS = 'getChatJoinRequests'
        GET_CHAT_LISTS_TO_ADD_CHAT = 'getChatListsToAddChat'
        GET_CHAT_MEMBER = 'getChatMember'
        GET_CHAT_MESSAGE_BY_DATE = 'getChatMessageByDate'
        GET_CHAT_MESSAGE_CALENDAR = 'getChatMessageCalendar'
        GET_CHAT_MESSAGE_COUNT = 'getChatMessageCount'
        GET_CHAT_NOTIFICATION_SETTINGS_EXCEPTIONS = 'getChatNotificationSettingsExceptions'
        GET_CHAT_PINNED_MESSAGE = 'getChatPinnedMessage'
        GET_CHAT_SCHEDULED_MESSAGES = 'getChatScheduledMessages'
        GET_CHAT_SPARSE_MESSAGE_POSITIONS = 'getChatSparseMessagePositions'
        GET_CHAT_SPONSORED_MESSAGE = 'getChatSponsoredMessage'
        GET_CHAT_STATISTICS = 'getChatStatistics'
        GET_CHATS = 'getChats'
        GET_COMMANDS = 'getCommands'
        GET_CONNECTED_WEBSITES = 'getConnectedWebsites'
        GET_CONTACTS = 'getContacts'
        GET_COUNTRIES = 'getCountries'
        GET_COUNTRY_CODE = 'getCountryCode'
        GET_CREATED_PUBLIC_CHATS = 'getCreatedPublicChats'
        GET_CURRENT_STATE = 'getCurrentState'
        GET_DATABASE_STATISTICS = 'getDatabaseStatistics'
        GET_DEEP_LINK_INFO = 'getDeepLinkInfo'
        GET_EMOJI_SUGGESTIONS_URL = 'getEmojiSuggestionsUrl'
        GET_EXTERNAL_LINK = 'getExternalLink'
        GET_EXTERNAL_LINK_INFO = 'getExternalLinkInfo'
        GET_FAVORITE_STICKERS = 'getFavoriteStickers'
        GET_FILE = 'getFile'
        GET_FILE_DOWNLOADED_PREFIX_SIZE = 'getFileDownloadedPrefixSize'
        GET_FILE_EXTENSION = 'getFileExtension'
        GET_FILE_MIME_TYPE = 'getFileMimeType'
        GET_GAME_HIGH_SCORES = 'getGameHighScores'
        GET_GROUP_CALL = 'getGroupCall'
        GET_GROUP_CALL_INVITE_LINK = 'getGroupCallInviteLink'
        GET_GROUP_CALL_STREAM_SEGMENT = 'getGroupCallStreamSegment'
        GET_GROUP_CALL_STREAMS = 'getGroupCallStreams'
        GET_GROUPS_IN_COMMON = 'getGroupsInCommon'
        GET_IMPORTED_CONTACT_COUNT = 'getImportedContactCount'
        GET_INACTIVE_SUPERGROUP_CHATS = 'getInactiveSupergroupChats'
        GET_INLINE_GAME_HIGH_SCORES = 'getInlineGameHighScores'
        GET_INLINE_QUERY_RESULTS = 'getInlineQueryResults'
        GET_INSTALLED_STICKER_SETS = 'getInstalledStickerSets'
        GET_INTERNAL_LINK_TYPE = 'getInternalLinkType'
        GET_JSON_STRING = 'getJsonString'
        GET_JSON_VALUE = 'getJsonValue'
        GET_LANGUAGE_PACK_INFO = 'getLanguagePackInfo'
        GET_LANGUAGE_PACK_STRING = 'getLanguagePackString'
        GET_LANGUAGE_PACK_STRINGS = 'getLanguagePackStrings'
        GET_LOCALIZATION_TARGET_INFO = 'getLocalizationTargetInfo'
        GET_LOG_STREAM = 'getLogStream'
        GET_LOG_TAG_VERBOSITY_LEVEL = 'getLogTagVerbosityLevel'
        GET_LOG_TAGS = 'getLogTags'
        GET_LOG_VERBOSITY_LEVEL = 'getLogVerbosityLevel'
        GET_LOGIN_URL = 'getLoginUrl'
        GET_LOGIN_URL_INFO = 'getLoginUrlInfo'
        GET_MAP_THUMBNAIL_FILE = 'getMapThumbnailFile'
        GET_MARKDOWN_TEXT = 'getMarkdownText'
        GET_ME = 'getMe'
        GET_MENU_BUTTON = 'getMenuButton'
        GET_MESSAGE = 'getMessage'
        GET_MESSAGE_ADDED_REACTIONS = 'getMessageAddedReactions'
        GET_MESSAGE_AVAILABLE_REACTIONS = 'getMessageAvailableReactions'
        GET_MESSAGE_EMBEDDING_CODE = 'getMessageEmbeddingCode'
        GET_MESSAGE_FILE_TYPE = 'getMessageFileType'
        GET_MESSAGE_IMPORT_CONFIRMATION_TEXT = 'getMessageImportConfirmationText'
        GET_MESSAGE_LINK = 'getMessageLink'
        GET_MESSAGE_LINK_INFO = 'getMessageLinkInfo'
        GET_MESSAGE_LOCALLY = 'getMessageLocally'
        GET_MESSAGE_PUBLIC_FORWARDS = 'getMessagePublicForwards'
        GET_MESSAGE_STATISTICS = 'getMessageStatistics'
        GET_MESSAGE_THREAD = 'getMessageThread'
        GET_MESSAGE_THREAD_HISTORY = 'getMessageThreadHistory'
        GET_MESSAGE_VIEWERS = 'getMessageViewers'
        GET_MESSAGES = 'getMessages'
        GET_NETWORK_STATISTICS = 'getNetworkStatistics'
        GET_OPTION = 'getOption'
        GET_PASSPORT_AUTHORIZATION_FORM = 'getPassportAuthorizationForm'
        GET_PASSPORT_AUTHORIZATION_FORM_AVAILABLE_ELEMENTS = 'getPassportAuthorizationFormAvailableElements'
        GET_PASSPORT_ELEMENT = 'getPassportElement'
        GET_PASSWORD_STATE = 'getPasswordState'
        GET_PAYMENT_FORM = 'getPaymentForm'
        GET_PAYMENT_RECEIPT = 'getPaymentReceipt'
        GET_PHONE_NUMBER_INFO = 'getPhoneNumberInfo'
        GET_PHONE_NUMBER_INFO_SYNC = 'getPhoneNumberInfoSync'
        GET_POLL_VOTERS = 'getPollVoters'
        GET_PREFERRED_COUNTRY_LANGUAGE = 'getPreferredCountryLanguage'
        GET_PROXIES = 'getProxies'
        GET_PROXY_LINK = 'getProxyLink'
        GET_PUSH_RECEIVER_ID = 'getPushReceiverId'
        GET_RECENT_INLINE_BOTS = 'getRecentInlineBots'
        GET_RECENT_STICKERS = 'getRecentStickers'
        GET_RECENTLY_OPENED_CHATS = 'getRecentlyOpenedChats'
        GET_RECENTLY_VISITED_T_ME_URLS = 'getRecentlyVisitedTMeUrls'
        GET_RECOMMENDED_CHAT_FILTERS = 'getRecommendedChatFilters'
        GET_RECOVERY_EMAIL_ADDRESS = 'getRecoveryEmailAddress'
        GET_REMOTE_FILE = 'getRemoteFile'
        GET_REPLIED_MESSAGE = 'getRepliedMessage'
        GET_SAVED_ANIMATIONS = 'getSavedAnimations'
        GET_SAVED_NOTIFICATION_SOUND = 'getSavedNotificationSound'
        GET_SAVED_NOTIFICATION_SOUNDS = 'getSavedNotificationSounds'
        GET_SAVED_ORDER_INFO = 'getSavedOrderInfo'
        GET_SCOPE_NOTIFICATION_SETTINGS = 'getScopeNotificationSettings'
        GET_SECRET_CHAT = 'getSecretChat'
        GET_STATISTICAL_GRAPH = 'getStatisticalGraph'
        GET_STICKER_EMOJIS = 'getStickerEmojis'
        GET_STICKER_SET = 'getStickerSet'
        GET_STICKERS = 'getStickers'
        GET_STORAGE_STATISTICS = 'getStorageStatistics'
        GET_STORAGE_STATISTICS_FAST = 'getStorageStatisticsFast'
        GET_SUGGESTED_FILE_NAME = 'getSuggestedFileName'
        GET_SUGGESTED_STICKER_SET_NAME = 'getSuggestedStickerSetName'
        GET_SUITABLE_DISCUSSION_CHATS = 'getSuitableDiscussionChats'
        GET_SUPERGROUP = 'getSupergroup'
        GET_SUPERGROUP_FULL_INFO = 'getSupergroupFullInfo'
        GET_SUPERGROUP_MEMBERS = 'getSupergroupMembers'
        GET_SUPPORT_USER = 'getSupportUser'
        GET_TEMPORARY_PASSWORD_STATE = 'getTemporaryPasswordState'
        GET_TEXT_ENTITIES = 'getTextEntities'
        GET_THEME_PARAMETERS_JSON_STRING = 'getThemeParametersJsonString'
        GET_TOP_CHATS = 'getTopChats'
        GET_TRENDING_STICKER_SETS = 'getTrendingStickerSets'
        GET_USER = 'getUser'
        GET_USER_FULL_INFO = 'getUserFullInfo'
        GET_USER_PRIVACY_SETTING_RULES = 'getUserPrivacySettingRules'
        GET_USER_PROFILE_PHOTOS = 'getUserProfilePhotos'
        GET_VIDEO_CHAT_AVAILABLE_PARTICIPANTS = 'getVideoChatAvailableParticipants'
        GET_VIDEO_CHAT_RTMP_URL = 'getVideoChatRtmpUrl'
        GET_WEB_APP_URL = 'getWebAppUrl'
        GET_WEB_PAGE_INSTANT_VIEW = 'getWebPageInstantView'
        GET_WEB_PAGE_PREVIEW = 'getWebPagePreview'
        GROUP_CALL = 'groupCall'
        GROUP_CALL_ID = 'groupCallId'
        GROUP_CALL_PARTICIPANT = 'groupCallParticipant'
        GROUP_CALL_PARTICIPANT_VIDEO_INFO = 'groupCallParticipantVideoInfo'
        GROUP_CALL_RECENT_SPEAKER = 'groupCallRecentSpeaker'
        GROUP_CALL_STREAM = 'groupCallStream'
        GROUP_CALL_STREAMS = 'groupCallStreams'
        GROUP_CALL_VIDEO_QUALITY = 'groupCallVideoQuality'
        GROUP_CALL_VIDEO_QUALITY_FULL = 'groupCallVideoQualityFull'
        GROUP_CALL_VIDEO_QUALITY_MEDIUM = 'groupCallVideoQualityMedium'
        GROUP_CALL_VIDEO_QUALITY_THUMBNAIL = 'groupCallVideoQualityThumbnail'
        GROUP_CALL_VIDEO_SOURCE_GROUP = 'groupCallVideoSourceGroup'
        HASHTAGS = 'hashtags'
        HIDE_SUGGESTED_ACTION = 'hideSuggestedAction'
        HTTP_URL = 'httpUrl'
        IDENTITY_DOCUMENT = 'identityDocument'
        IMPORT_CONTACTS = 'importContacts'
        IMPORT_MESSAGES = 'importMessages'
        IMPORTED_CONTACTS = 'importedContacts'
        INLINE_KEYBOARD_BUTTON = 'inlineKeyboardButton'
        INLINE_KEYBOARD_BUTTON_TYPE = 'inlineKeyboardButtonType'
        INLINE_KEYBOARD_BUTTON_TYPE_BUY = 'inlineKeyboardButtonTypeBuy'
        INLINE_KEYBOARD_BUTTON_TYPE_CALLBACK = 'inlineKeyboardButtonTypeCallback'
        INLINE_KEYBOARD_BUTTON_TYPE_CALLBACK_GAME = 'inlineKeyboardButtonTypeCallbackGame'
        INLINE_KEYBOARD_BUTTON_TYPE_CALLBACK_WITH_PASSWORD = 'inlineKeyboardButtonTypeCallbackWithPassword'
        INLINE_KEYBOARD_BUTTON_TYPE_LOGIN_URL = 'inlineKeyboardButtonTypeLoginUrl'
        INLINE_KEYBOARD_BUTTON_TYPE_SWITCH_INLINE = 'inlineKeyboardButtonTypeSwitchInline'
        INLINE_KEYBOARD_BUTTON_TYPE_URL = 'inlineKeyboardButtonTypeUrl'
        INLINE_KEYBOARD_BUTTON_TYPE_USER = 'inlineKeyboardButtonTypeUser'
        INLINE_KEYBOARD_BUTTON_TYPE_WEB_APP = 'inlineKeyboardButtonTypeWebApp'
        INLINE_QUERY_RESULT = 'inlineQueryResult'
        INLINE_QUERY_RESULT_ANIMATION = 'inlineQueryResultAnimation'
        INLINE_QUERY_RESULT_ARTICLE = 'inlineQueryResultArticle'
        INLINE_QUERY_RESULT_AUDIO = 'inlineQueryResultAudio'
        INLINE_QUERY_RESULT_CONTACT = 'inlineQueryResultContact'
        INLINE_QUERY_RESULT_DOCUMENT = 'inlineQueryResultDocument'
        INLINE_QUERY_RESULT_GAME = 'inlineQueryResultGame'
        INLINE_QUERY_RESULT_LOCATION = 'inlineQueryResultLocation'
        INLINE_QUERY_RESULT_PHOTO = 'inlineQueryResultPhoto'
        INLINE_QUERY_RESULT_STICKER = 'inlineQueryResultSticker'
        INLINE_QUERY_RESULT_VENUE = 'inlineQueryResultVenue'
        INLINE_QUERY_RESULT_VIDEO = 'inlineQueryResultVideo'
        INLINE_QUERY_RESULT_VOICE_NOTE = 'inlineQueryResultVoiceNote'
        INLINE_QUERY_RESULTS = 'inlineQueryResults'
        INPUT_BACKGROUND = 'inputBackground'
        INPUT_BACKGROUND_LOCAL = 'inputBackgroundLocal'
        INPUT_BACKGROUND_REMOTE = 'inputBackgroundRemote'
        INPUT_CHAT_PHOTO = 'inputChatPhoto'
        INPUT_CHAT_PHOTO_ANIMATION = 'inputChatPhotoAnimation'
        INPUT_CHAT_PHOTO_PREVIOUS = 'inputChatPhotoPrevious'
        INPUT_CHAT_PHOTO_STATIC = 'inputChatPhotoStatic'
        INPUT_CREDENTIALS = 'inputCredentials'
        INPUT_CREDENTIALS_APPLE_PAY = 'inputCredentialsApplePay'
        INPUT_CREDENTIALS_GOOGLE_PAY = 'inputCredentialsGooglePay'
        INPUT_CREDENTIALS_NEW = 'inputCredentialsNew'
        INPUT_CREDENTIALS_SAVED = 'inputCredentialsSaved'
        INPUT_FILE = 'inputFile'
        INPUT_FILE_GENERATED = 'inputFileGenerated'
        INPUT_FILE_ID = 'inputFileId'
        INPUT_FILE_LOCAL = 'inputFileLocal'
        INPUT_FILE_REMOTE = 'inputFileRemote'
        INPUT_IDENTITY_DOCUMENT = 'inputIdentityDocument'
        INPUT_INLINE_QUERY_RESULT = 'inputInlineQueryResult'
        INPUT_INLINE_QUERY_RESULT_ANIMATION = 'inputInlineQueryResultAnimation'
        INPUT_INLINE_QUERY_RESULT_ARTICLE = 'inputInlineQueryResultArticle'
        INPUT_INLINE_QUERY_RESULT_AUDIO = 'inputInlineQueryResultAudio'
        INPUT_INLINE_QUERY_RESULT_CONTACT = 'inputInlineQueryResultContact'
        INPUT_INLINE_QUERY_RESULT_DOCUMENT = 'inputInlineQueryResultDocument'
        INPUT_INLINE_QUERY_RESULT_GAME = 'inputInlineQueryResultGame'
        INPUT_INLINE_QUERY_RESULT_LOCATION = 'inputInlineQueryResultLocation'
        INPUT_INLINE_QUERY_RESULT_PHOTO = 'inputInlineQueryResultPhoto'
        INPUT_INLINE_QUERY_RESULT_STICKER = 'inputInlineQueryResultSticker'
        INPUT_INLINE_QUERY_RESULT_VENUE = 'inputInlineQueryResultVenue'
        INPUT_INLINE_QUERY_RESULT_VIDEO = 'inputInlineQueryResultVideo'
        INPUT_INLINE_QUERY_RESULT_VOICE_NOTE = 'inputInlineQueryResultVoiceNote'
        INPUT_MESSAGE_CONTENT = 'inputMessageContent'
        INPUT_MESSAGE_ANIMATION = 'inputMessageAnimation'
        INPUT_MESSAGE_AUDIO = 'inputMessageAudio'
        INPUT_MESSAGE_CONTACT = 'inputMessageContact'
        INPUT_MESSAGE_DICE = 'inputMessageDice'
        INPUT_MESSAGE_DOCUMENT = 'inputMessageDocument'
        INPUT_MESSAGE_FORWARDED = 'inputMessageForwarded'
        INPUT_MESSAGE_GAME = 'inputMessageGame'
        INPUT_MESSAGE_INVOICE = 'inputMessageInvoice'
        INPUT_MESSAGE_LOCATION = 'inputMessageLocation'
        INPUT_MESSAGE_PHOTO = 'inputMessagePhoto'
        INPUT_MESSAGE_POLL = 'inputMessagePoll'
        INPUT_MESSAGE_STICKER = 'inputMessageSticker'
        INPUT_MESSAGE_TEXT = 'inputMessageText'
        INPUT_MESSAGE_VENUE = 'inputMessageVenue'
        INPUT_MESSAGE_VIDEO = 'inputMessageVideo'
        INPUT_MESSAGE_VIDEO_NOTE = 'inputMessageVideoNote'
        INPUT_MESSAGE_VOICE_NOTE = 'inputMessageVoiceNote'
        INPUT_PASSPORT_ELEMENT = 'inputPassportElement'
        INPUT_PASSPORT_ELEMENT_ADDRESS = 'inputPassportElementAddress'
        INPUT_PASSPORT_ELEMENT_BANK_STATEMENT = 'inputPassportElementBankStatement'
        INPUT_PASSPORT_ELEMENT_DRIVER_LICENSE = 'inputPassportElementDriverLicense'
        INPUT_PASSPORT_ELEMENT_EMAIL_ADDRESS = 'inputPassportElementEmailAddress'
        INPUT_PASSPORT_ELEMENT_IDENTITY_CARD = 'inputPassportElementIdentityCard'
        INPUT_PASSPORT_ELEMENT_INTERNAL_PASSPORT = 'inputPassportElementInternalPassport'
        INPUT_PASSPORT_ELEMENT_PASSPORT = 'inputPassportElementPassport'
        INPUT_PASSPORT_ELEMENT_PASSPORT_REGISTRATION = 'inputPassportElementPassportRegistration'
        INPUT_PASSPORT_ELEMENT_PERSONAL_DETAILS = 'inputPassportElementPersonalDetails'
        INPUT_PASSPORT_ELEMENT_PHONE_NUMBER = 'inputPassportElementPhoneNumber'
        INPUT_PASSPORT_ELEMENT_RENTAL_AGREEMENT = 'inputPassportElementRentalAgreement'
        INPUT_PASSPORT_ELEMENT_TEMPORARY_REGISTRATION = 'inputPassportElementTemporaryRegistration'
        INPUT_PASSPORT_ELEMENT_UTILITY_BILL = 'inputPassportElementUtilityBill'
        INPUT_PASSPORT_ELEMENT_ERROR = 'inputPassportElementError'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE = 'inputPassportElementErrorSource'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_DATA_FIELD = 'inputPassportElementErrorSourceDataField'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_FILE = 'inputPassportElementErrorSourceFile'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_FILES = 'inputPassportElementErrorSourceFiles'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_FRONT_SIDE = 'inputPassportElementErrorSourceFrontSide'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_REVERSE_SIDE = 'inputPassportElementErrorSourceReverseSide'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_SELFIE = 'inputPassportElementErrorSourceSelfie'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_TRANSLATION_FILE = 'inputPassportElementErrorSourceTranslationFile'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_TRANSLATION_FILES = 'inputPassportElementErrorSourceTranslationFiles'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_UNSPECIFIED = 'inputPassportElementErrorSourceUnspecified'
        INPUT_PERSONAL_DOCUMENT = 'inputPersonalDocument'
        INPUT_STICKER = 'inputSticker'
        INPUT_THUMBNAIL = 'inputThumbnail'
        INTERNAL_LINK_TYPE = 'internalLinkType'
        INTERNAL_LINK_TYPE_ACTIVE_SESSIONS = 'internalLinkTypeActiveSessions'
        INTERNAL_LINK_TYPE_ATTACHMENT_MENU_BOT = 'internalLinkTypeAttachmentMenuBot'
        INTERNAL_LINK_TYPE_AUTHENTICATION_CODE = 'internalLinkTypeAuthenticationCode'
        INTERNAL_LINK_TYPE_BACKGROUND = 'internalLinkTypeBackground'
        INTERNAL_LINK_TYPE_BOT_ADD_TO_CHANNEL = 'internalLinkTypeBotAddToChannel'
        INTERNAL_LINK_TYPE_BOT_START = 'internalLinkTypeBotStart'
        INTERNAL_LINK_TYPE_BOT_START_IN_GROUP = 'internalLinkTypeBotStartInGroup'
        INTERNAL_LINK_TYPE_CHANGE_PHONE_NUMBER = 'internalLinkTypeChangePhoneNumber'
        INTERNAL_LINK_TYPE_CHAT_INVITE = 'internalLinkTypeChatInvite'
        INTERNAL_LINK_TYPE_FILTER_SETTINGS = 'internalLinkTypeFilterSettings'
        INTERNAL_LINK_TYPE_GAME = 'internalLinkTypeGame'
        INTERNAL_LINK_TYPE_LANGUAGE_PACK = 'internalLinkTypeLanguagePack'
        INTERNAL_LINK_TYPE_LANGUAGE_SETTINGS = 'internalLinkTypeLanguageSettings'
        INTERNAL_LINK_TYPE_MESSAGE = 'internalLinkTypeMessage'
        INTERNAL_LINK_TYPE_MESSAGE_DRAFT = 'internalLinkTypeMessageDraft'
        INTERNAL_LINK_TYPE_PASSPORT_DATA_REQUEST = 'internalLinkTypePassportDataRequest'
        INTERNAL_LINK_TYPE_PHONE_NUMBER_CONFIRMATION = 'internalLinkTypePhoneNumberConfirmation'
        INTERNAL_LINK_TYPE_PRIVACY_AND_SECURITY_SETTINGS = 'internalLinkTypePrivacyAndSecuritySettings'
        INTERNAL_LINK_TYPE_PROXY = 'internalLinkTypeProxy'
        INTERNAL_LINK_TYPE_PUBLIC_CHAT = 'internalLinkTypePublicChat'
        INTERNAL_LINK_TYPE_QR_CODE_AUTHENTICATION = 'internalLinkTypeQrCodeAuthentication'
        INTERNAL_LINK_TYPE_SETTINGS = 'internalLinkTypeSettings'
        INTERNAL_LINK_TYPE_STICKER_SET = 'internalLinkTypeStickerSet'
        INTERNAL_LINK_TYPE_THEME = 'internalLinkTypeTheme'
        INTERNAL_LINK_TYPE_THEME_SETTINGS = 'internalLinkTypeThemeSettings'
        INTERNAL_LINK_TYPE_UNKNOWN_DEEP_LINK = 'internalLinkTypeUnknownDeepLink'
        INTERNAL_LINK_TYPE_UNSUPPORTED_PROXY = 'internalLinkTypeUnsupportedProxy'
        INTERNAL_LINK_TYPE_USER_PHONE_NUMBER = 'internalLinkTypeUserPhoneNumber'
        INTERNAL_LINK_TYPE_VIDEO_CHAT = 'internalLinkTypeVideoChat'
        INVITE_GROUP_CALL_PARTICIPANTS = 'inviteGroupCallParticipants'
        INVOICE = 'invoice'
        JOIN_CHAT = 'joinChat'
        JOIN_CHAT_BY_INVITE_LINK = 'joinChatByInviteLink'
        JOIN_GROUP_CALL = 'joinGroupCall'
        JSON_VALUE = 'jsonValue'
        JSON_VALUE_ARRAY = 'jsonValueArray'
        JSON_VALUE_BOOLEAN = 'jsonValueBoolean'
        JSON_VALUE_NULL = 'jsonValueNull'
        JSON_VALUE_NUMBER = 'jsonValueNumber'
        JSON_VALUE_OBJECT = 'jsonValueObject'
        JSON_VALUE_STRING = 'jsonValueString'
        KEYBOARD_BUTTON = 'keyboardButton'
        KEYBOARD_BUTTON_TYPE = 'keyboardButtonType'
        KEYBOARD_BUTTON_TYPE_REQUEST_LOCATION = 'keyboardButtonTypeRequestLocation'
        KEYBOARD_BUTTON_TYPE_REQUEST_PHONE_NUMBER = 'keyboardButtonTypeRequestPhoneNumber'
        KEYBOARD_BUTTON_TYPE_REQUEST_POLL = 'keyboardButtonTypeRequestPoll'
        KEYBOARD_BUTTON_TYPE_TEXT = 'keyboardButtonTypeText'
        KEYBOARD_BUTTON_TYPE_WEB_APP = 'keyboardButtonTypeWebApp'
        LABELED_PRICE_PART = 'labeledPricePart'
        LANGUAGE_PACK_INFO = 'languagePackInfo'
        LANGUAGE_PACK_STRING = 'languagePackString'
        LANGUAGE_PACK_STRING_VALUE = 'languagePackStringValue'
        LANGUAGE_PACK_STRING_VALUE_DELETED = 'languagePackStringValueDeleted'
        LANGUAGE_PACK_STRING_VALUE_ORDINARY = 'languagePackStringValueOrdinary'
        LANGUAGE_PACK_STRING_VALUE_PLURALIZED = 'languagePackStringValuePluralized'
        LANGUAGE_PACK_STRINGS = 'languagePackStrings'
        LEAVE_CHAT = 'leaveChat'
        LEAVE_GROUP_CALL = 'leaveGroupCall'
        LOAD_CHATS = 'loadChats'
        LOAD_GROUP_CALL_PARTICIPANTS = 'loadGroupCallParticipants'
        LOCAL_FILE = 'localFile'
        LOCALIZATION_TARGET_INFO = 'localizationTargetInfo'
        LOCATION = 'location'
        LOG_OUT = 'logOut'
        LOG_STREAM = 'logStream'
        LOG_STREAM_DEFAULT = 'logStreamDefault'
        LOG_STREAM_EMPTY = 'logStreamEmpty'
        LOG_STREAM_FILE = 'logStreamFile'
        LOG_TAGS = 'logTags'
        LOG_VERBOSITY_LEVEL = 'logVerbosityLevel'
        LOGIN_URL_INFO = 'loginUrlInfo'
        LOGIN_URL_INFO_OPEN = 'loginUrlInfoOpen'
        LOGIN_URL_INFO_REQUEST_CONFIRMATION = 'loginUrlInfoRequestConfirmation'
        MASK_POINT = 'maskPoint'
        MASK_POINT_CHIN = 'maskPointChin'
        MASK_POINT_EYES = 'maskPointEyes'
        MASK_POINT_FOREHEAD = 'maskPointForehead'
        MASK_POINT_MOUTH = 'maskPointMouth'
        MASK_POSITION = 'maskPosition'
        MESSAGE = 'message'
        MESSAGE_CALENDAR = 'messageCalendar'
        MESSAGE_CALENDAR_DAY = 'messageCalendarDay'
        MESSAGE_CONTENT = 'messageContent'
        MESSAGE_ANIMATED_EMOJI = 'messageAnimatedEmoji'
        MESSAGE_ANIMATION = 'messageAnimation'
        MESSAGE_AUDIO = 'messageAudio'
        MESSAGE_BASIC_GROUP_CHAT_CREATE = 'messageBasicGroupChatCreate'
        MESSAGE_CALL = 'messageCall'
        MESSAGE_CHAT_ADD_MEMBERS = 'messageChatAddMembers'
        MESSAGE_CHAT_CHANGE_PHOTO = 'messageChatChangePhoto'
        MESSAGE_CHAT_CHANGE_TITLE = 'messageChatChangeTitle'
        MESSAGE_CHAT_DELETE_MEMBER = 'messageChatDeleteMember'
        MESSAGE_CHAT_DELETE_PHOTO = 'messageChatDeletePhoto'
        MESSAGE_CHAT_JOIN_BY_LINK = 'messageChatJoinByLink'
        MESSAGE_CHAT_JOIN_BY_REQUEST = 'messageChatJoinByRequest'
        MESSAGE_CHAT_SET_THEME = 'messageChatSetTheme'
        MESSAGE_CHAT_SET_TTL = 'messageChatSetTtl'
        MESSAGE_CHAT_UPGRADE_FROM = 'messageChatUpgradeFrom'
        MESSAGE_CHAT_UPGRADE_TO = 'messageChatUpgradeTo'
        MESSAGE_CONTACT = 'messageContact'
        MESSAGE_CONTACT_REGISTERED = 'messageContactRegistered'
        MESSAGE_CUSTOM_SERVICE_ACTION = 'messageCustomServiceAction'
        MESSAGE_DICE = 'messageDice'
        MESSAGE_DOCUMENT = 'messageDocument'
        MESSAGE_EXPIRED_PHOTO = 'messageExpiredPhoto'
        MESSAGE_EXPIRED_VIDEO = 'messageExpiredVideo'
        MESSAGE_GAME = 'messageGame'
        MESSAGE_GAME_SCORE = 'messageGameScore'
        MESSAGE_INVITE_VIDEO_CHAT_PARTICIPANTS = 'messageInviteVideoChatParticipants'
        MESSAGE_INVOICE = 'messageInvoice'
        MESSAGE_LOCATION = 'messageLocation'
        MESSAGE_PASSPORT_DATA_RECEIVED = 'messagePassportDataReceived'
        MESSAGE_PASSPORT_DATA_SENT = 'messagePassportDataSent'
        MESSAGE_PAYMENT_SUCCESSFUL = 'messagePaymentSuccessful'
        MESSAGE_PAYMENT_SUCCESSFUL_BOT = 'messagePaymentSuccessfulBot'
        MESSAGE_PHOTO = 'messagePhoto'
        MESSAGE_PIN_MESSAGE = 'messagePinMessage'
        MESSAGE_POLL = 'messagePoll'
        MESSAGE_PROXIMITY_ALERT_TRIGGERED = 'messageProximityAlertTriggered'
        MESSAGE_SCREENSHOT_TAKEN = 'messageScreenshotTaken'
        MESSAGE_STICKER = 'messageSticker'
        MESSAGE_SUPERGROUP_CHAT_CREATE = 'messageSupergroupChatCreate'
        MESSAGE_TEXT = 'messageText'
        MESSAGE_UNSUPPORTED = 'messageUnsupported'
        MESSAGE_VENUE = 'messageVenue'
        MESSAGE_VIDEO = 'messageVideo'
        MESSAGE_VIDEO_CHAT_ENDED = 'messageVideoChatEnded'
        MESSAGE_VIDEO_CHAT_SCHEDULED = 'messageVideoChatScheduled'
        MESSAGE_VIDEO_CHAT_STARTED = 'messageVideoChatStarted'
        MESSAGE_VIDEO_NOTE = 'messageVideoNote'
        MESSAGE_VOICE_NOTE = 'messageVoiceNote'
        MESSAGE_WEB_APP_DATA_RECEIVED = 'messageWebAppDataReceived'
        MESSAGE_WEB_APP_DATA_SENT = 'messageWebAppDataSent'
        MESSAGE_WEBSITE_CONNECTED = 'messageWebsiteConnected'
        MESSAGE_COPY_OPTIONS = 'messageCopyOptions'
        MESSAGE_FILE_TYPE = 'messageFileType'
        MESSAGE_FILE_TYPE_GROUP = 'messageFileTypeGroup'
        MESSAGE_FILE_TYPE_PRIVATE = 'messageFileTypePrivate'
        MESSAGE_FILE_TYPE_UNKNOWN = 'messageFileTypeUnknown'
        MESSAGE_FORWARD_INFO = 'messageForwardInfo'
        MESSAGE_FORWARD_ORIGIN = 'messageForwardOrigin'
        MESSAGE_FORWARD_ORIGIN_CHANNEL = 'messageForwardOriginChannel'
        MESSAGE_FORWARD_ORIGIN_CHAT = 'messageForwardOriginChat'
        MESSAGE_FORWARD_ORIGIN_HIDDEN_USER = 'messageForwardOriginHiddenUser'
        MESSAGE_FORWARD_ORIGIN_MESSAGE_IMPORT = 'messageForwardOriginMessageImport'
        MESSAGE_FORWARD_ORIGIN_USER = 'messageForwardOriginUser'
        MESSAGE_INTERACTION_INFO = 'messageInteractionInfo'
        MESSAGE_LINK = 'messageLink'
        MESSAGE_LINK_INFO = 'messageLinkInfo'
        MESSAGE_POSITION = 'messagePosition'
        MESSAGE_POSITIONS = 'messagePositions'
        MESSAGE_REACTION = 'messageReaction'
        MESSAGE_REPLY_INFO = 'messageReplyInfo'
        MESSAGE_SCHEDULING_STATE = 'messageSchedulingState'
        MESSAGE_SCHEDULING_STATE_SEND_AT_DATE = 'messageSchedulingStateSendAtDate'
        MESSAGE_SCHEDULING_STATE_SEND_WHEN_ONLINE = 'messageSchedulingStateSendWhenOnline'
        MESSAGE_SEND_OPTIONS = 'messageSendOptions'
        MESSAGE_SENDER = 'messageSender'
        MESSAGE_SENDER_CHAT = 'messageSenderChat'
        MESSAGE_SENDER_USER = 'messageSenderUser'
        MESSAGE_SENDERS = 'messageSenders'
        MESSAGE_SENDING_STATE = 'messageSendingState'
        MESSAGE_SENDING_STATE_FAILED = 'messageSendingStateFailed'
        MESSAGE_SENDING_STATE_PENDING = 'messageSendingStatePending'
        MESSAGE_STATISTICS = 'messageStatistics'
        MESSAGE_THREAD_INFO = 'messageThreadInfo'
        MESSAGES = 'messages'
        MINITHUMBNAIL = 'minithumbnail'
        NETWORK_STATISTICS = 'networkStatistics'
        NETWORK_STATISTICS_ENTRY = 'networkStatisticsEntry'
        NETWORK_STATISTICS_ENTRY_CALL = 'networkStatisticsEntryCall'
        NETWORK_STATISTICS_ENTRY_FILE = 'networkStatisticsEntryFile'
        NETWORK_TYPE = 'networkType'
        NETWORK_TYPE_MOBILE = 'networkTypeMobile'
        NETWORK_TYPE_MOBILE_ROAMING = 'networkTypeMobileRoaming'
        NETWORK_TYPE_NONE = 'networkTypeNone'
        NETWORK_TYPE_OTHER = 'networkTypeOther'
        NETWORK_TYPE_WI_FI = 'networkTypeWiFi'
        NOTIFICATION = 'notification'
        NOTIFICATION_GROUP = 'notificationGroup'
        NOTIFICATION_GROUP_TYPE = 'notificationGroupType'
        NOTIFICATION_GROUP_TYPE_CALLS = 'notificationGroupTypeCalls'
        NOTIFICATION_GROUP_TYPE_MENTIONS = 'notificationGroupTypeMentions'
        NOTIFICATION_GROUP_TYPE_MESSAGES = 'notificationGroupTypeMessages'
        NOTIFICATION_GROUP_TYPE_SECRET_CHAT = 'notificationGroupTypeSecretChat'
        NOTIFICATION_SETTINGS_SCOPE = 'notificationSettingsScope'
        NOTIFICATION_SETTINGS_SCOPE_CHANNEL_CHATS = 'notificationSettingsScopeChannelChats'
        NOTIFICATION_SETTINGS_SCOPE_GROUP_CHATS = 'notificationSettingsScopeGroupChats'
        NOTIFICATION_SETTINGS_SCOPE_PRIVATE_CHATS = 'notificationSettingsScopePrivateChats'
        NOTIFICATION_SOUND = 'notificationSound'
        NOTIFICATION_SOUNDS = 'notificationSounds'
        NOTIFICATION_TYPE = 'notificationType'
        NOTIFICATION_TYPE_NEW_CALL = 'notificationTypeNewCall'
        NOTIFICATION_TYPE_NEW_MESSAGE = 'notificationTypeNewMessage'
        NOTIFICATION_TYPE_NEW_PUSH_MESSAGE = 'notificationTypeNewPushMessage'
        NOTIFICATION_TYPE_NEW_SECRET_CHAT = 'notificationTypeNewSecretChat'
        OK = 'ok'
        OPEN_CHAT = 'openChat'
        OPEN_MESSAGE_CONTENT = 'openMessageContent'
        OPEN_WEB_APP = 'openWebApp'
        OPTIMIZE_STORAGE = 'optimizeStorage'
        OPTION_VALUE = 'optionValue'
        OPTION_VALUE_BOOLEAN = 'optionValueBoolean'
        OPTION_VALUE_EMPTY = 'optionValueEmpty'
        OPTION_VALUE_INTEGER = 'optionValueInteger'
        OPTION_VALUE_STRING = 'optionValueString'
        ORDER_INFO = 'orderInfo'
        PAGE_BLOCK = 'pageBlock'
        PAGE_BLOCK_ANCHOR = 'pageBlockAnchor'
        PAGE_BLOCK_ANIMATION = 'pageBlockAnimation'
        PAGE_BLOCK_AUDIO = 'pageBlockAudio'
        PAGE_BLOCK_AUTHOR_DATE = 'pageBlockAuthorDate'
        PAGE_BLOCK_BLOCK_QUOTE = 'pageBlockBlockQuote'
        PAGE_BLOCK_CHAT_LINK = 'pageBlockChatLink'
        PAGE_BLOCK_COLLAGE = 'pageBlockCollage'
        PAGE_BLOCK_COVER = 'pageBlockCover'
        PAGE_BLOCK_DETAILS = 'pageBlockDetails'
        PAGE_BLOCK_DIVIDER = 'pageBlockDivider'
        PAGE_BLOCK_EMBEDDED = 'pageBlockEmbedded'
        PAGE_BLOCK_EMBEDDED_POST = 'pageBlockEmbeddedPost'
        PAGE_BLOCK_FOOTER = 'pageBlockFooter'
        PAGE_BLOCK_HEADER = 'pageBlockHeader'
        PAGE_BLOCK_KICKER = 'pageBlockKicker'
        PAGE_BLOCK_LIST = 'pageBlockList'
        PAGE_BLOCK_MAP = 'pageBlockMap'
        PAGE_BLOCK_PARAGRAPH = 'pageBlockParagraph'
        PAGE_BLOCK_PHOTO = 'pageBlockPhoto'
        PAGE_BLOCK_PREFORMATTED = 'pageBlockPreformatted'
        PAGE_BLOCK_PULL_QUOTE = 'pageBlockPullQuote'
        PAGE_BLOCK_RELATED_ARTICLES = 'pageBlockRelatedArticles'
        PAGE_BLOCK_SLIDESHOW = 'pageBlockSlideshow'
        PAGE_BLOCK_SUBHEADER = 'pageBlockSubheader'
        PAGE_BLOCK_SUBTITLE = 'pageBlockSubtitle'
        PAGE_BLOCK_TABLE = 'pageBlockTable'
        PAGE_BLOCK_TITLE = 'pageBlockTitle'
        PAGE_BLOCK_VIDEO = 'pageBlockVideo'
        PAGE_BLOCK_VOICE_NOTE = 'pageBlockVoiceNote'
        PAGE_BLOCK_CAPTION = 'pageBlockCaption'
        PAGE_BLOCK_HORIZONTAL_ALIGNMENT = 'pageBlockHorizontalAlignment'
        PAGE_BLOCK_HORIZONTAL_ALIGNMENT_CENTER = 'pageBlockHorizontalAlignmentCenter'
        PAGE_BLOCK_HORIZONTAL_ALIGNMENT_LEFT = 'pageBlockHorizontalAlignmentLeft'
        PAGE_BLOCK_HORIZONTAL_ALIGNMENT_RIGHT = 'pageBlockHorizontalAlignmentRight'
        PAGE_BLOCK_RELATED_ARTICLE = 'pageBlockRelatedArticle'
        PAGE_BLOCK_TABLE_CELL = 'pageBlockTableCell'
        PAGE_BLOCK_VERTICAL_ALIGNMENT = 'pageBlockVerticalAlignment'
        PAGE_BLOCK_VERTICAL_ALIGNMENT_BOTTOM = 'pageBlockVerticalAlignmentBottom'
        PAGE_BLOCK_VERTICAL_ALIGNMENT_MIDDLE = 'pageBlockVerticalAlignmentMiddle'
        PAGE_BLOCK_VERTICAL_ALIGNMENT_TOP = 'pageBlockVerticalAlignmentTop'
        PARSE_MARKDOWN = 'parseMarkdown'
        PARSE_TEXT_ENTITIES = 'parseTextEntities'
        PASSPORT_AUTHORIZATION_FORM = 'passportAuthorizationForm'
        PASSPORT_ELEMENT = 'passportElement'
        PASSPORT_ELEMENT_ADDRESS = 'passportElementAddress'
        PASSPORT_ELEMENT_BANK_STATEMENT = 'passportElementBankStatement'
        PASSPORT_ELEMENT_DRIVER_LICENSE = 'passportElementDriverLicense'
        PASSPORT_ELEMENT_EMAIL_ADDRESS = 'passportElementEmailAddress'
        PASSPORT_ELEMENT_IDENTITY_CARD = 'passportElementIdentityCard'
        PASSPORT_ELEMENT_INTERNAL_PASSPORT = 'passportElementInternalPassport'
        PASSPORT_ELEMENT_PASSPORT = 'passportElementPassport'
        PASSPORT_ELEMENT_PASSPORT_REGISTRATION = 'passportElementPassportRegistration'
        PASSPORT_ELEMENT_PERSONAL_DETAILS = 'passportElementPersonalDetails'
        PASSPORT_ELEMENT_PHONE_NUMBER = 'passportElementPhoneNumber'
        PASSPORT_ELEMENT_RENTAL_AGREEMENT = 'passportElementRentalAgreement'
        PASSPORT_ELEMENT_TEMPORARY_REGISTRATION = 'passportElementTemporaryRegistration'
        PASSPORT_ELEMENT_UTILITY_BILL = 'passportElementUtilityBill'
        PASSPORT_ELEMENT_ERROR = 'passportElementError'
        PASSPORT_ELEMENT_ERROR_SOURCE = 'passportElementErrorSource'
        PASSPORT_ELEMENT_ERROR_SOURCE_DATA_FIELD = 'passportElementErrorSourceDataField'
        PASSPORT_ELEMENT_ERROR_SOURCE_FILE = 'passportElementErrorSourceFile'
        PASSPORT_ELEMENT_ERROR_SOURCE_FILES = 'passportElementErrorSourceFiles'
        PASSPORT_ELEMENT_ERROR_SOURCE_FRONT_SIDE = 'passportElementErrorSourceFrontSide'
        PASSPORT_ELEMENT_ERROR_SOURCE_REVERSE_SIDE = 'passportElementErrorSourceReverseSide'
        PASSPORT_ELEMENT_ERROR_SOURCE_SELFIE = 'passportElementErrorSourceSelfie'
        PASSPORT_ELEMENT_ERROR_SOURCE_TRANSLATION_FILE = 'passportElementErrorSourceTranslationFile'
        PASSPORT_ELEMENT_ERROR_SOURCE_TRANSLATION_FILES = 'passportElementErrorSourceTranslationFiles'
        PASSPORT_ELEMENT_ERROR_SOURCE_UNSPECIFIED = 'passportElementErrorSourceUnspecified'
        PASSPORT_ELEMENT_TYPE = 'passportElementType'
        PASSPORT_ELEMENT_TYPE_ADDRESS = 'passportElementTypeAddress'
        PASSPORT_ELEMENT_TYPE_BANK_STATEMENT = 'passportElementTypeBankStatement'
        PASSPORT_ELEMENT_TYPE_DRIVER_LICENSE = 'passportElementTypeDriverLicense'
        PASSPORT_ELEMENT_TYPE_EMAIL_ADDRESS = 'passportElementTypeEmailAddress'
        PASSPORT_ELEMENT_TYPE_IDENTITY_CARD = 'passportElementTypeIdentityCard'
        PASSPORT_ELEMENT_TYPE_INTERNAL_PASSPORT = 'passportElementTypeInternalPassport'
        PASSPORT_ELEMENT_TYPE_PASSPORT = 'passportElementTypePassport'
        PASSPORT_ELEMENT_TYPE_PASSPORT_REGISTRATION = 'passportElementTypePassportRegistration'
        PASSPORT_ELEMENT_TYPE_PERSONAL_DETAILS = 'passportElementTypePersonalDetails'
        PASSPORT_ELEMENT_TYPE_PHONE_NUMBER = 'passportElementTypePhoneNumber'
        PASSPORT_ELEMENT_TYPE_RENTAL_AGREEMENT = 'passportElementTypeRentalAgreement'
        PASSPORT_ELEMENT_TYPE_TEMPORARY_REGISTRATION = 'passportElementTypeTemporaryRegistration'
        PASSPORT_ELEMENT_TYPE_UTILITY_BILL = 'passportElementTypeUtilityBill'
        PASSPORT_ELEMENTS = 'passportElements'
        PASSPORT_ELEMENTS_WITH_ERRORS = 'passportElementsWithErrors'
        PASSPORT_REQUIRED_ELEMENT = 'passportRequiredElement'
        PASSPORT_SUITABLE_ELEMENT = 'passportSuitableElement'
        PASSWORD_STATE = 'passwordState'
        PAYMENT_FORM = 'paymentForm'
        PAYMENT_RECEIPT = 'paymentReceipt'
        PAYMENT_RESULT = 'paymentResult'
        PAYMENTS_PROVIDER_STRIPE = 'paymentsProviderStripe'
        PERSONAL_DETAILS = 'personalDetails'
        PERSONAL_DOCUMENT = 'personalDocument'
        PHONE_NUMBER_AUTHENTICATION_SETTINGS = 'phoneNumberAuthenticationSettings'
        PHONE_NUMBER_INFO = 'phoneNumberInfo'
        PHOTO = 'photo'
        PHOTO_SIZE = 'photoSize'
        PIN_CHAT_MESSAGE = 'pinChatMessage'
        PING_PROXY = 'pingProxy'
        POINT = 'point'
        POLL = 'poll'
        POLL_OPTION = 'pollOption'
        POLL_TYPE = 'pollType'
        POLL_TYPE_QUIZ = 'pollTypeQuiz'
        POLL_TYPE_REGULAR = 'pollTypeRegular'
        PROCESS_CHAT_JOIN_REQUEST = 'processChatJoinRequest'
        PROCESS_CHAT_JOIN_REQUESTS = 'processChatJoinRequests'
        PROCESS_PUSH_NOTIFICATION = 'processPushNotification'
        PROFILE_PHOTO = 'profilePhoto'
        PROXIES = 'proxies'
        PROXY = 'proxy'
        PROXY_TYPE = 'proxyType'
        PROXY_TYPE_HTTP = 'proxyTypeHttp'
        PROXY_TYPE_MTPROTO = 'proxyTypeMtproto'
        PROXY_TYPE_SOCKS5 = 'proxyTypeSocks5'
        PUBLIC_CHAT_TYPE = 'publicChatType'
        PUBLIC_CHAT_TYPE_HAS_USERNAME = 'publicChatTypeHasUsername'
        PUBLIC_CHAT_TYPE_IS_LOCATION_BASED = 'publicChatTypeIsLocationBased'
        PUSH_MESSAGE_CONTENT = 'pushMessageContent'
        PUSH_MESSAGE_CONTENT_ANIMATION = 'pushMessageContentAnimation'
        PUSH_MESSAGE_CONTENT_AUDIO = 'pushMessageContentAudio'
        PUSH_MESSAGE_CONTENT_BASIC_GROUP_CHAT_CREATE = 'pushMessageContentBasicGroupChatCreate'
        PUSH_MESSAGE_CONTENT_CHAT_ADD_MEMBERS = 'pushMessageContentChatAddMembers'
        PUSH_MESSAGE_CONTENT_CHAT_CHANGE_PHOTO = 'pushMessageContentChatChangePhoto'
        PUSH_MESSAGE_CONTENT_CHAT_CHANGE_TITLE = 'pushMessageContentChatChangeTitle'
        PUSH_MESSAGE_CONTENT_CHAT_DELETE_MEMBER = 'pushMessageContentChatDeleteMember'
        PUSH_MESSAGE_CONTENT_CHAT_JOIN_BY_LINK = 'pushMessageContentChatJoinByLink'
        PUSH_MESSAGE_CONTENT_CHAT_JOIN_BY_REQUEST = 'pushMessageContentChatJoinByRequest'
        PUSH_MESSAGE_CONTENT_CHAT_SET_THEME = 'pushMessageContentChatSetTheme'
        PUSH_MESSAGE_CONTENT_CONTACT = 'pushMessageContentContact'
        PUSH_MESSAGE_CONTENT_CONTACT_REGISTERED = 'pushMessageContentContactRegistered'
        PUSH_MESSAGE_CONTENT_DOCUMENT = 'pushMessageContentDocument'
        PUSH_MESSAGE_CONTENT_GAME = 'pushMessageContentGame'
        PUSH_MESSAGE_CONTENT_GAME_SCORE = 'pushMessageContentGameScore'
        PUSH_MESSAGE_CONTENT_HIDDEN = 'pushMessageContentHidden'
        PUSH_MESSAGE_CONTENT_INVOICE = 'pushMessageContentInvoice'
        PUSH_MESSAGE_CONTENT_LOCATION = 'pushMessageContentLocation'
        PUSH_MESSAGE_CONTENT_MEDIA_ALBUM = 'pushMessageContentMediaAlbum'
        PUSH_MESSAGE_CONTENT_MESSAGE_FORWARDS = 'pushMessageContentMessageForwards'
        PUSH_MESSAGE_CONTENT_PHOTO = 'pushMessageContentPhoto'
        PUSH_MESSAGE_CONTENT_POLL = 'pushMessageContentPoll'
        PUSH_MESSAGE_CONTENT_SCREENSHOT_TAKEN = 'pushMessageContentScreenshotTaken'
        PUSH_MESSAGE_CONTENT_STICKER = 'pushMessageContentSticker'
        PUSH_MESSAGE_CONTENT_TEXT = 'pushMessageContentText'
        PUSH_MESSAGE_CONTENT_VIDEO = 'pushMessageContentVideo'
        PUSH_MESSAGE_CONTENT_VIDEO_NOTE = 'pushMessageContentVideoNote'
        PUSH_MESSAGE_CONTENT_VOICE_NOTE = 'pushMessageContentVoiceNote'
        PUSH_RECEIVER_ID = 'pushReceiverId'
        REACTION = 'reaction'
        READ_ALL_CHAT_MENTIONS = 'readAllChatMentions'
        READ_ALL_CHAT_REACTIONS = 'readAllChatReactions'
        READ_FILE_PART = 'readFilePart'
        RECOMMENDED_CHAT_FILTER = 'recommendedChatFilter'
        RECOMMENDED_CHAT_FILTERS = 'recommendedChatFilters'
        RECOVER_AUTHENTICATION_PASSWORD = 'recoverAuthenticationPassword'
        RECOVER_PASSWORD = 'recoverPassword'
        RECOVERY_EMAIL_ADDRESS = 'recoveryEmailAddress'
        REGISTER_DEVICE = 'registerDevice'
        REGISTER_USER = 'registerUser'
        REMOTE_FILE = 'remoteFile'
        REMOVE_ALL_FILES_FROM_DOWNLOADS = 'removeAllFilesFromDownloads'
        REMOVE_BACKGROUND = 'removeBackground'
        REMOVE_CHAT_ACTION_BAR = 'removeChatActionBar'
        REMOVE_CONTACTS = 'removeContacts'
        REMOVE_FAVORITE_STICKER = 'removeFavoriteSticker'
        REMOVE_FILE_FROM_DOWNLOADS = 'removeFileFromDownloads'
        REMOVE_NOTIFICATION = 'removeNotification'
        REMOVE_NOTIFICATION_GROUP = 'removeNotificationGroup'
        REMOVE_PROXY = 'removeProxy'
        REMOVE_RECENT_HASHTAG = 'removeRecentHashtag'
        REMOVE_RECENT_STICKER = 'removeRecentSticker'
        REMOVE_RECENTLY_FOUND_CHAT = 'removeRecentlyFoundChat'
        REMOVE_SAVED_ANIMATION = 'removeSavedAnimation'
        REMOVE_SAVED_NOTIFICATION_SOUND = 'removeSavedNotificationSound'
        REMOVE_STICKER_FROM_SET = 'removeStickerFromSet'
        REMOVE_TOP_CHAT = 'removeTopChat'
        REORDER_CHAT_FILTERS = 'reorderChatFilters'
        REORDER_INSTALLED_STICKER_SETS = 'reorderInstalledStickerSets'
        REPLACE_PRIMARY_CHAT_INVITE_LINK = 'replacePrimaryChatInviteLink'
        REPLACE_VIDEO_CHAT_RTMP_URL = 'replaceVideoChatRtmpUrl'
        REPLY_MARKUP = 'replyMarkup'
        REPLY_MARKUP_FORCE_REPLY = 'replyMarkupForceReply'
        REPLY_MARKUP_INLINE_KEYBOARD = 'replyMarkupInlineKeyboard'
        REPLY_MARKUP_REMOVE_KEYBOARD = 'replyMarkupRemoveKeyboard'
        REPLY_MARKUP_SHOW_KEYBOARD = 'replyMarkupShowKeyboard'
        REPORT_CHAT = 'reportChat'
        REPORT_CHAT_PHOTO = 'reportChatPhoto'
        REPORT_SUPERGROUP_SPAM = 'reportSupergroupSpam'
        REQUEST_AUTHENTICATION_PASSWORD_RECOVERY = 'requestAuthenticationPasswordRecovery'
        REQUEST_PASSWORD_RECOVERY = 'requestPasswordRecovery'
        REQUEST_QR_CODE_AUTHENTICATION = 'requestQrCodeAuthentication'
        RESEND_AUTHENTICATION_CODE = 'resendAuthenticationCode'
        RESEND_CHANGE_PHONE_NUMBER_CODE = 'resendChangePhoneNumberCode'
        RESEND_EMAIL_ADDRESS_VERIFICATION_CODE = 'resendEmailAddressVerificationCode'
        RESEND_MESSAGES = 'resendMessages'
        RESEND_PHONE_NUMBER_CONFIRMATION_CODE = 'resendPhoneNumberConfirmationCode'
        RESEND_PHONE_NUMBER_VERIFICATION_CODE = 'resendPhoneNumberVerificationCode'
        RESEND_RECOVERY_EMAIL_ADDRESS_CODE = 'resendRecoveryEmailAddressCode'
        RESET_ALL_NOTIFICATION_SETTINGS = 'resetAllNotificationSettings'
        RESET_BACKGROUNDS = 'resetBackgrounds'
        RESET_NETWORK_STATISTICS = 'resetNetworkStatistics'
        RESET_PASSWORD = 'resetPassword'
        RESET_PASSWORD_RESULT = 'resetPasswordResult'
        RESET_PASSWORD_RESULT_DECLINED = 'resetPasswordResultDeclined'
        RESET_PASSWORD_RESULT_OK = 'resetPasswordResultOk'
        RESET_PASSWORD_RESULT_PENDING = 'resetPasswordResultPending'
        REVOKE_CHAT_INVITE_LINK = 'revokeChatInviteLink'
        REVOKE_GROUP_CALL_INVITE_LINK = 'revokeGroupCallInviteLink'
        RICH_TEXT = 'richText'
        RICH_TEXT_ANCHOR = 'richTextAnchor'
        RICH_TEXT_ANCHOR_LINK = 'richTextAnchorLink'
        RICH_TEXT_BOLD = 'richTextBold'
        RICH_TEXT_EMAIL_ADDRESS = 'richTextEmailAddress'
        RICH_TEXT_FIXED = 'richTextFixed'
        RICH_TEXT_ICON = 'richTextIcon'
        RICH_TEXT_ITALIC = 'richTextItalic'
        RICH_TEXT_MARKED = 'richTextMarked'
        RICH_TEXT_PHONE_NUMBER = 'richTextPhoneNumber'
        RICH_TEXT_PLAIN = 'richTextPlain'
        RICH_TEXT_REFERENCE = 'richTextReference'
        RICH_TEXT_STRIKETHROUGH = 'richTextStrikethrough'
        RICH_TEXT_SUBSCRIPT = 'richTextSubscript'
        RICH_TEXT_SUPERSCRIPT = 'richTextSuperscript'
        RICH_TEXT_UNDERLINE = 'richTextUnderline'
        RICH_TEXT_URL = 'richTextUrl'
        RICH_TEXTS = 'richTexts'
        RTMP_URL = 'rtmpUrl'
        SAVE_APPLICATION_LOG_EVENT = 'saveApplicationLogEvent'
        SAVED_CREDENTIALS = 'savedCredentials'
        SCOPE_NOTIFICATION_SETTINGS = 'scopeNotificationSettings'
        SEARCH_BACKGROUND = 'searchBackground'
        SEARCH_CALL_MESSAGES = 'searchCallMessages'
        SEARCH_CHAT_MEMBERS = 'searchChatMembers'
        SEARCH_CHAT_MESSAGES = 'searchChatMessages'
        SEARCH_CHAT_RECENT_LOCATION_MESSAGES = 'searchChatRecentLocationMessages'
        SEARCH_CHATS = 'searchChats'
        SEARCH_CHATS_NEARBY = 'searchChatsNearby'
        SEARCH_CHATS_ON_SERVER = 'searchChatsOnServer'
        SEARCH_CONTACTS = 'searchContacts'
        SEARCH_EMOJIS = 'searchEmojis'
        SEARCH_FILE_DOWNLOADS = 'searchFileDownloads'
        SEARCH_HASHTAGS = 'searchHashtags'
        SEARCH_INSTALLED_STICKER_SETS = 'searchInstalledStickerSets'
        SEARCH_MESSAGES = 'searchMessages'
        SEARCH_MESSAGES_FILTER = 'searchMessagesFilter'
        SEARCH_MESSAGES_FILTER_ANIMATION = 'searchMessagesFilterAnimation'
        SEARCH_MESSAGES_FILTER_AUDIO = 'searchMessagesFilterAudio'
        SEARCH_MESSAGES_FILTER_CHAT_PHOTO = 'searchMessagesFilterChatPhoto'
        SEARCH_MESSAGES_FILTER_DOCUMENT = 'searchMessagesFilterDocument'
        SEARCH_MESSAGES_FILTER_EMPTY = 'searchMessagesFilterEmpty'
        SEARCH_MESSAGES_FILTER_FAILED_TO_SEND = 'searchMessagesFilterFailedToSend'
        SEARCH_MESSAGES_FILTER_MENTION = 'searchMessagesFilterMention'
        SEARCH_MESSAGES_FILTER_PHOTO = 'searchMessagesFilterPhoto'
        SEARCH_MESSAGES_FILTER_PHOTO_AND_VIDEO = 'searchMessagesFilterPhotoAndVideo'
        SEARCH_MESSAGES_FILTER_PINNED = 'searchMessagesFilterPinned'
        SEARCH_MESSAGES_FILTER_UNREAD_MENTION = 'searchMessagesFilterUnreadMention'
        SEARCH_MESSAGES_FILTER_UNREAD_REACTION = 'searchMessagesFilterUnreadReaction'
        SEARCH_MESSAGES_FILTER_URL = 'searchMessagesFilterUrl'
        SEARCH_MESSAGES_FILTER_VIDEO = 'searchMessagesFilterVideo'
        SEARCH_MESSAGES_FILTER_VIDEO_NOTE = 'searchMessagesFilterVideoNote'
        SEARCH_MESSAGES_FILTER_VOICE_AND_VIDEO_NOTE = 'searchMessagesFilterVoiceAndVideoNote'
        SEARCH_MESSAGES_FILTER_VOICE_NOTE = 'searchMessagesFilterVoiceNote'
        SEARCH_OUTGOING_DOCUMENT_MESSAGES = 'searchOutgoingDocumentMessages'
        SEARCH_PUBLIC_CHAT = 'searchPublicChat'
        SEARCH_PUBLIC_CHATS = 'searchPublicChats'
        SEARCH_SECRET_MESSAGES = 'searchSecretMessages'
        SEARCH_STICKER_SET = 'searchStickerSet'
        SEARCH_STICKER_SETS = 'searchStickerSets'
        SEARCH_STICKERS = 'searchStickers'
        SEARCH_USER_BY_PHONE_NUMBER = 'searchUserByPhoneNumber'
        SECONDS = 'seconds'
        SECRET_CHAT = 'secretChat'
        SECRET_CHAT_STATE = 'secretChatState'
        SECRET_CHAT_STATE_CLOSED = 'secretChatStateClosed'
        SECRET_CHAT_STATE_PENDING = 'secretChatStatePending'
        SECRET_CHAT_STATE_READY = 'secretChatStateReady'
        SEND_BOT_START_MESSAGE = 'sendBotStartMessage'
        SEND_CALL_DEBUG_INFORMATION = 'sendCallDebugInformation'
        SEND_CALL_RATING = 'sendCallRating'
        SEND_CALL_SIGNALING_DATA = 'sendCallSignalingData'
        SEND_CHAT_ACTION = 'sendChatAction'
        SEND_CHAT_SCREENSHOT_TAKEN_NOTIFICATION = 'sendChatScreenshotTakenNotification'
        SEND_CUSTOM_REQUEST = 'sendCustomRequest'
        SEND_EMAIL_ADDRESS_VERIFICATION_CODE = 'sendEmailAddressVerificationCode'
        SEND_INLINE_QUERY_RESULT_MESSAGE = 'sendInlineQueryResultMessage'
        SEND_MESSAGE = 'sendMessage'
        SEND_MESSAGE_ALBUM = 'sendMessageAlbum'
        SEND_PASSPORT_AUTHORIZATION_FORM = 'sendPassportAuthorizationForm'
        SEND_PAYMENT_FORM = 'sendPaymentForm'
        SEND_PHONE_NUMBER_CONFIRMATION_CODE = 'sendPhoneNumberConfirmationCode'
        SEND_PHONE_NUMBER_VERIFICATION_CODE = 'sendPhoneNumberVerificationCode'
        SEND_WEB_APP_DATA = 'sendWebAppData'
        SENT_WEB_APP_MESSAGE = 'sentWebAppMessage'
        SESSION = 'session'
        SESSIONS = 'sessions'
        SET_ACCOUNT_TTL = 'setAccountTtl'
        SET_ALARM = 'setAlarm'
        SET_AUTHENTICATION_PHONE_NUMBER = 'setAuthenticationPhoneNumber'
        SET_AUTO_DOWNLOAD_SETTINGS = 'setAutoDownloadSettings'
        SET_BACKGROUND = 'setBackground'
        SET_BIO = 'setBio'
        SET_BOT_UPDATES_STATUS = 'setBotUpdatesStatus'
        SET_CHAT_AVAILABLE_REACTIONS = 'setChatAvailableReactions'
        SET_CHAT_CLIENT_DATA = 'setChatClientData'
        SET_CHAT_DESCRIPTION = 'setChatDescription'
        SET_CHAT_DISCUSSION_GROUP = 'setChatDiscussionGroup'
        SET_CHAT_DRAFT_MESSAGE = 'setChatDraftMessage'
        SET_CHAT_LOCATION = 'setChatLocation'
        SET_CHAT_MEMBER_STATUS = 'setChatMemberStatus'
        SET_CHAT_MESSAGE_SENDER = 'setChatMessageSender'
        SET_CHAT_MESSAGE_TTL = 'setChatMessageTtl'
        SET_CHAT_NOTIFICATION_SETTINGS = 'setChatNotificationSettings'
        SET_CHAT_PERMISSIONS = 'setChatPermissions'
        SET_CHAT_PHOTO = 'setChatPhoto'
        SET_CHAT_SLOW_MODE_DELAY = 'setChatSlowModeDelay'
        SET_CHAT_THEME = 'setChatTheme'
        SET_CHAT_TITLE = 'setChatTitle'
        SET_COMMANDS = 'setCommands'
        SET_CUSTOM_LANGUAGE_PACK = 'setCustomLanguagePack'
        SET_CUSTOM_LANGUAGE_PACK_STRING = 'setCustomLanguagePackString'
        SET_DATABASE_ENCRYPTION_KEY = 'setDatabaseEncryptionKey'
        SET_DEFAULT_CHANNEL_ADMINISTRATOR_RIGHTS = 'setDefaultChannelAdministratorRights'
        SET_DEFAULT_GROUP_ADMINISTRATOR_RIGHTS = 'setDefaultGroupAdministratorRights'
        SET_FILE_GENERATION_PROGRESS = 'setFileGenerationProgress'
        SET_GAME_SCORE = 'setGameScore'
        SET_GROUP_CALL_PARTICIPANT_IS_SPEAKING = 'setGroupCallParticipantIsSpeaking'
        SET_GROUP_CALL_PARTICIPANT_VOLUME_LEVEL = 'setGroupCallParticipantVolumeLevel'
        SET_GROUP_CALL_TITLE = 'setGroupCallTitle'
        SET_INACTIVE_SESSION_TTL = 'setInactiveSessionTtl'
        SET_INLINE_GAME_SCORE = 'setInlineGameScore'
        SET_LOCATION = 'setLocation'
        SET_LOG_STREAM = 'setLogStream'
        SET_LOG_TAG_VERBOSITY_LEVEL = 'setLogTagVerbosityLevel'
        SET_LOG_VERBOSITY_LEVEL = 'setLogVerbosityLevel'
        SET_MENU_BUTTON = 'setMenuButton'
        SET_MESSAGE_REACTION = 'setMessageReaction'
        SET_NAME = 'setName'
        SET_NETWORK_TYPE = 'setNetworkType'
        SET_OPTION = 'setOption'
        SET_PASSPORT_ELEMENT = 'setPassportElement'
        SET_PASSPORT_ELEMENT_ERRORS = 'setPassportElementErrors'
        SET_PASSWORD = 'setPassword'
        SET_PINNED_CHATS = 'setPinnedChats'
        SET_POLL_ANSWER = 'setPollAnswer'
        SET_PROFILE_PHOTO = 'setProfilePhoto'
        SET_RECOVERY_EMAIL_ADDRESS = 'setRecoveryEmailAddress'
        SET_SCOPE_NOTIFICATION_SETTINGS = 'setScopeNotificationSettings'
        SET_STICKER_POSITION_IN_SET = 'setStickerPositionInSet'
        SET_STICKER_SET_THUMBNAIL = 'setStickerSetThumbnail'
        SET_SUPERGROUP_STICKER_SET = 'setSupergroupStickerSet'
        SET_SUPERGROUP_USERNAME = 'setSupergroupUsername'
        SET_TDLIB_PARAMETERS = 'setTdlibParameters'
        SET_USER_PRIVACY_SETTING_RULES = 'setUserPrivacySettingRules'
        SET_USERNAME = 'setUsername'
        SET_VIDEO_CHAT_DEFAULT_PARTICIPANT = 'setVideoChatDefaultParticipant'
        SHARE_PHONE_NUMBER = 'sharePhoneNumber'
        SHIPPING_OPTION = 'shippingOption'
        SPONSORED_MESSAGE = 'sponsoredMessage'
        START_GROUP_CALL_RECORDING = 'startGroupCallRecording'
        START_GROUP_CALL_SCREEN_SHARING = 'startGroupCallScreenSharing'
        START_SCHEDULED_GROUP_CALL = 'startScheduledGroupCall'
        STATISTICAL_GRAPH = 'statisticalGraph'
        STATISTICAL_GRAPH_ASYNC = 'statisticalGraphAsync'
        STATISTICAL_GRAPH_DATA = 'statisticalGraphData'
        STATISTICAL_GRAPH_ERROR = 'statisticalGraphError'
        STATISTICAL_VALUE = 'statisticalValue'
        STICKER = 'sticker'
        STICKER_SET = 'stickerSet'
        STICKER_SET_INFO = 'stickerSetInfo'
        STICKER_SETS = 'stickerSets'
        STICKER_TYPE = 'stickerType'
        STICKER_TYPE_ANIMATED = 'stickerTypeAnimated'
        STICKER_TYPE_MASK = 'stickerTypeMask'
        STICKER_TYPE_STATIC = 'stickerTypeStatic'
        STICKER_TYPE_VIDEO = 'stickerTypeVideo'
        STICKERS = 'stickers'
        STOP_POLL = 'stopPoll'
        STORAGE_STATISTICS = 'storageStatistics'
        STORAGE_STATISTICS_BY_CHAT = 'storageStatisticsByChat'
        STORAGE_STATISTICS_BY_FILE_TYPE = 'storageStatisticsByFileType'
        STORAGE_STATISTICS_FAST = 'storageStatisticsFast'
        SUGGESTED_ACTION = 'suggestedAction'
        SUGGESTED_ACTION_CHECK_PASSWORD = 'suggestedActionCheckPassword'
        SUGGESTED_ACTION_CHECK_PHONE_NUMBER = 'suggestedActionCheckPhoneNumber'
        SUGGESTED_ACTION_CONVERT_TO_BROADCAST_GROUP = 'suggestedActionConvertToBroadcastGroup'
        SUGGESTED_ACTION_ENABLE_ARCHIVE_AND_MUTE_NEW_CHATS = 'suggestedActionEnableArchiveAndMuteNewChats'
        SUGGESTED_ACTION_SET_PASSWORD = 'suggestedActionSetPassword'
        SUGGESTED_ACTION_VIEW_CHECKS_HINT = 'suggestedActionViewChecksHint'
        SUPERGROUP = 'supergroup'
        SUPERGROUP_FULL_INFO = 'supergroupFullInfo'
        SUPERGROUP_MEMBERS_FILTER = 'supergroupMembersFilter'
        SUPERGROUP_MEMBERS_FILTER_ADMINISTRATORS = 'supergroupMembersFilterAdministrators'
        SUPERGROUP_MEMBERS_FILTER_BANNED = 'supergroupMembersFilterBanned'
        SUPERGROUP_MEMBERS_FILTER_BOTS = 'supergroupMembersFilterBots'
        SUPERGROUP_MEMBERS_FILTER_CONTACTS = 'supergroupMembersFilterContacts'
        SUPERGROUP_MEMBERS_FILTER_MENTION = 'supergroupMembersFilterMention'
        SUPERGROUP_MEMBERS_FILTER_RECENT = 'supergroupMembersFilterRecent'
        SUPERGROUP_MEMBERS_FILTER_RESTRICTED = 'supergroupMembersFilterRestricted'
        SUPERGROUP_MEMBERS_FILTER_SEARCH = 'supergroupMembersFilterSearch'
        SYNCHRONIZE_LANGUAGE_PACK = 'synchronizeLanguagePack'
        T_ME_URL = 'tMeUrl'
        T_ME_URL_TYPE = 'tMeUrlType'
        T_ME_URL_TYPE_CHAT_INVITE = 'tMeUrlTypeChatInvite'
        T_ME_URL_TYPE_STICKER_SET = 'tMeUrlTypeStickerSet'
        T_ME_URL_TYPE_SUPERGROUP = 'tMeUrlTypeSupergroup'
        T_ME_URL_TYPE_USER = 'tMeUrlTypeUser'
        T_ME_URLS = 'tMeUrls'
        TDLIB_PARAMETERS = 'tdlibParameters'
        TEMPORARY_PASSWORD_STATE = 'temporaryPasswordState'
        TERMINATE_ALL_OTHER_SESSIONS = 'terminateAllOtherSessions'
        TERMINATE_SESSION = 'terminateSession'
        TERMS_OF_SERVICE = 'termsOfService'
        TEST_BYTES = 'testBytes'
        TEST_CALL_BYTES = 'testCallBytes'
        TEST_CALL_EMPTY = 'testCallEmpty'
        TEST_CALL_STRING = 'testCallString'
        TEST_CALL_VECTOR_INT = 'testCallVectorInt'
        TEST_CALL_VECTOR_INT_OBJECT = 'testCallVectorIntObject'
        TEST_CALL_VECTOR_STRING = 'testCallVectorString'
        TEST_CALL_VECTOR_STRING_OBJECT = 'testCallVectorStringObject'
        TEST_GET_DIFFERENCE = 'testGetDifference'
        TEST_INT = 'testInt'
        TEST_NETWORK = 'testNetwork'
        TEST_PROXY = 'testProxy'
        TEST_RETURN_ERROR = 'testReturnError'
        TEST_SQUARE_INT = 'testSquareInt'
        TEST_STRING = 'testString'
        TEST_USE_UPDATE = 'testUseUpdate'
        TEST_VECTOR_INT = 'testVectorInt'
        TEST_VECTOR_INT_OBJECT = 'testVectorIntObject'
        TEST_VECTOR_STRING = 'testVectorString'
        TEST_VECTOR_STRING_OBJECT = 'testVectorStringObject'
        TEXT = 'text'
        TEXT_ENTITIES = 'textEntities'
        TEXT_ENTITY = 'textEntity'
        TEXT_ENTITY_TYPE = 'textEntityType'
        TEXT_ENTITY_TYPE_BANK_CARD_NUMBER = 'textEntityTypeBankCardNumber'
        TEXT_ENTITY_TYPE_BOLD = 'textEntityTypeBold'
        TEXT_ENTITY_TYPE_BOT_COMMAND = 'textEntityTypeBotCommand'
        TEXT_ENTITY_TYPE_CASHTAG = 'textEntityTypeCashtag'
        TEXT_ENTITY_TYPE_CODE = 'textEntityTypeCode'
        TEXT_ENTITY_TYPE_EMAIL_ADDRESS = 'textEntityTypeEmailAddress'
        TEXT_ENTITY_TYPE_HASHTAG = 'textEntityTypeHashtag'
        TEXT_ENTITY_TYPE_ITALIC = 'textEntityTypeItalic'
        TEXT_ENTITY_TYPE_MEDIA_TIMESTAMP = 'textEntityTypeMediaTimestamp'
        TEXT_ENTITY_TYPE_MENTION = 'textEntityTypeMention'
        TEXT_ENTITY_TYPE_MENTION_NAME = 'textEntityTypeMentionName'
        TEXT_ENTITY_TYPE_PHONE_NUMBER = 'textEntityTypePhoneNumber'
        TEXT_ENTITY_TYPE_PRE = 'textEntityTypePre'
        TEXT_ENTITY_TYPE_PRE_CODE = 'textEntityTypePreCode'
        TEXT_ENTITY_TYPE_SPOILER = 'textEntityTypeSpoiler'
        TEXT_ENTITY_TYPE_STRIKETHROUGH = 'textEntityTypeStrikethrough'
        TEXT_ENTITY_TYPE_TEXT_URL = 'textEntityTypeTextUrl'
        TEXT_ENTITY_TYPE_UNDERLINE = 'textEntityTypeUnderline'
        TEXT_ENTITY_TYPE_URL = 'textEntityTypeUrl'
        TEXT_PARSE_MODE = 'textParseMode'
        TEXT_PARSE_MODE_HTML = 'textParseModeHTML'
        TEXT_PARSE_MODE_MARKDOWN = 'textParseModeMarkdown'
        THEME_PARAMETERS = 'themeParameters'
        THEME_SETTINGS = 'themeSettings'
        THUMBNAIL = 'thumbnail'
        THUMBNAIL_FORMAT = 'thumbnailFormat'
        THUMBNAIL_FORMAT_GIF = 'thumbnailFormatGif'
        THUMBNAIL_FORMAT_JPEG = 'thumbnailFormatJpeg'
        THUMBNAIL_FORMAT_MPEG4 = 'thumbnailFormatMpeg4'
        THUMBNAIL_FORMAT_PNG = 'thumbnailFormatPng'
        THUMBNAIL_FORMAT_TGS = 'thumbnailFormatTgs'
        THUMBNAIL_FORMAT_WEBM = 'thumbnailFormatWebm'
        THUMBNAIL_FORMAT_WEBP = 'thumbnailFormatWebp'
        TOGGLE_ALL_DOWNLOADS_ARE_PAUSED = 'toggleAllDownloadsArePaused'
        TOGGLE_BOT_IS_ADDED_TO_ATTACHMENT_MENU = 'toggleBotIsAddedToAttachmentMenu'
        TOGGLE_CHAT_DEFAULT_DISABLE_NOTIFICATION = 'toggleChatDefaultDisableNotification'
        TOGGLE_CHAT_HAS_PROTECTED_CONTENT = 'toggleChatHasProtectedContent'
        TOGGLE_CHAT_IS_MARKED_AS_UNREAD = 'toggleChatIsMarkedAsUnread'
        TOGGLE_CHAT_IS_PINNED = 'toggleChatIsPinned'
        TOGGLE_DOWNLOAD_IS_PAUSED = 'toggleDownloadIsPaused'
        TOGGLE_GROUP_CALL_ENABLED_START_NOTIFICATION = 'toggleGroupCallEnabledStartNotification'
        TOGGLE_GROUP_CALL_IS_MY_VIDEO_ENABLED = 'toggleGroupCallIsMyVideoEnabled'
        TOGGLE_GROUP_CALL_IS_MY_VIDEO_PAUSED = 'toggleGroupCallIsMyVideoPaused'
        TOGGLE_GROUP_CALL_MUTE_NEW_PARTICIPANTS = 'toggleGroupCallMuteNewParticipants'
        TOGGLE_GROUP_CALL_PARTICIPANT_IS_HAND_RAISED = 'toggleGroupCallParticipantIsHandRaised'
        TOGGLE_GROUP_CALL_PARTICIPANT_IS_MUTED = 'toggleGroupCallParticipantIsMuted'
        TOGGLE_GROUP_CALL_SCREEN_SHARING_IS_PAUSED = 'toggleGroupCallScreenSharingIsPaused'
        TOGGLE_MESSAGE_SENDER_IS_BLOCKED = 'toggleMessageSenderIsBlocked'
        TOGGLE_SESSION_CAN_ACCEPT_CALLS = 'toggleSessionCanAcceptCalls'
        TOGGLE_SESSION_CAN_ACCEPT_SECRET_CHATS = 'toggleSessionCanAcceptSecretChats'
        TOGGLE_SUPERGROUP_IS_ALL_HISTORY_AVAILABLE = 'toggleSupergroupIsAllHistoryAvailable'
        TOGGLE_SUPERGROUP_IS_BROADCAST_GROUP = 'toggleSupergroupIsBroadcastGroup'
        TOGGLE_SUPERGROUP_SIGN_MESSAGES = 'toggleSupergroupSignMessages'
        TOP_CHAT_CATEGORY = 'topChatCategory'
        TOP_CHAT_CATEGORY_BOTS = 'topChatCategoryBots'
        TOP_CHAT_CATEGORY_CALLS = 'topChatCategoryCalls'
        TOP_CHAT_CATEGORY_CHANNELS = 'topChatCategoryChannels'
        TOP_CHAT_CATEGORY_FORWARD_CHATS = 'topChatCategoryForwardChats'
        TOP_CHAT_CATEGORY_GROUPS = 'topChatCategoryGroups'
        TOP_CHAT_CATEGORY_INLINE_BOTS = 'topChatCategoryInlineBots'
        TOP_CHAT_CATEGORY_USERS = 'topChatCategoryUsers'
        TRANSFER_CHAT_OWNERSHIP = 'transferChatOwnership'
        TRANSLATE_TEXT = 'translateText'
        UNPIN_ALL_CHAT_MESSAGES = 'unpinAllChatMessages'
        UNPIN_CHAT_MESSAGE = 'unpinChatMessage'
        UNREAD_REACTION = 'unreadReaction'
        UPDATE = 'update'
        UPDATE_ACTIVE_NOTIFICATIONS = 'updateActiveNotifications'
        UPDATE_ANIMATED_EMOJI_MESSAGE_CLICKED = 'updateAnimatedEmojiMessageClicked'
        UPDATE_ANIMATION_SEARCH_PARAMETERS = 'updateAnimationSearchParameters'
        UPDATE_ATTACHMENT_MENU_BOTS = 'updateAttachmentMenuBots'
        UPDATE_AUTHORIZATION_STATE = 'updateAuthorizationState'
        UPDATE_BASIC_GROUP = 'updateBasicGroup'
        UPDATE_BASIC_GROUP_FULL_INFO = 'updateBasicGroupFullInfo'
        UPDATE_CALL = 'updateCall'
        UPDATE_CHAT_ACTION = 'updateChatAction'
        UPDATE_CHAT_ACTION_BAR = 'updateChatActionBar'
        UPDATE_CHAT_AVAILABLE_REACTIONS = 'updateChatAvailableReactions'
        UPDATE_CHAT_DEFAULT_DISABLE_NOTIFICATION = 'updateChatDefaultDisableNotification'
        UPDATE_CHAT_DRAFT_MESSAGE = 'updateChatDraftMessage'
        UPDATE_CHAT_FILTERS = 'updateChatFilters'
        UPDATE_CHAT_HAS_PROTECTED_CONTENT = 'updateChatHasProtectedContent'
        UPDATE_CHAT_HAS_SCHEDULED_MESSAGES = 'updateChatHasScheduledMessages'
        UPDATE_CHAT_IS_BLOCKED = 'updateChatIsBlocked'
        UPDATE_CHAT_IS_MARKED_AS_UNREAD = 'updateChatIsMarkedAsUnread'
        UPDATE_CHAT_LAST_MESSAGE = 'updateChatLastMessage'
        UPDATE_CHAT_MEMBER = 'updateChatMember'
        UPDATE_CHAT_MESSAGE_SENDER = 'updateChatMessageSender'
        UPDATE_CHAT_MESSAGE_TTL = 'updateChatMessageTtl'
        UPDATE_CHAT_NOTIFICATION_SETTINGS = 'updateChatNotificationSettings'
        UPDATE_CHAT_ONLINE_MEMBER_COUNT = 'updateChatOnlineMemberCount'
        UPDATE_CHAT_PENDING_JOIN_REQUESTS = 'updateChatPendingJoinRequests'
        UPDATE_CHAT_PERMISSIONS = 'updateChatPermissions'
        UPDATE_CHAT_PHOTO = 'updateChatPhoto'
        UPDATE_CHAT_POSITION = 'updateChatPosition'
        UPDATE_CHAT_READ_INBOX = 'updateChatReadInbox'
        UPDATE_CHAT_READ_OUTBOX = 'updateChatReadOutbox'
        UPDATE_CHAT_REPLY_MARKUP = 'updateChatReplyMarkup'
        UPDATE_CHAT_THEME = 'updateChatTheme'
        UPDATE_CHAT_THEMES = 'updateChatThemes'
        UPDATE_CHAT_TITLE = 'updateChatTitle'
        UPDATE_CHAT_UNREAD_MENTION_COUNT = 'updateChatUnreadMentionCount'
        UPDATE_CHAT_UNREAD_REACTION_COUNT = 'updateChatUnreadReactionCount'
        UPDATE_CHAT_VIDEO_CHAT = 'updateChatVideoChat'
        UPDATE_CONNECTION_STATE = 'updateConnectionState'
        UPDATE_DELETE_MESSAGES = 'updateDeleteMessages'
        UPDATE_DICE_EMOJIS = 'updateDiceEmojis'
        UPDATE_FAVORITE_STICKERS = 'updateFavoriteStickers'
        UPDATE_FILE = 'updateFile'
        UPDATE_FILE_ADDED_TO_DOWNLOADS = 'updateFileAddedToDownloads'
        UPDATE_FILE_DOWNLOAD = 'updateFileDownload'
        UPDATE_FILE_DOWNLOADS = 'updateFileDownloads'
        UPDATE_FILE_GENERATION_START = 'updateFileGenerationStart'
        UPDATE_FILE_GENERATION_STOP = 'updateFileGenerationStop'
        UPDATE_FILE_REMOVED_FROM_DOWNLOADS = 'updateFileRemovedFromDownloads'
        UPDATE_GROUP_CALL = 'updateGroupCall'
        UPDATE_GROUP_CALL_PARTICIPANT = 'updateGroupCallParticipant'
        UPDATE_HAVE_PENDING_NOTIFICATIONS = 'updateHavePendingNotifications'
        UPDATE_INSTALLED_STICKER_SETS = 'updateInstalledStickerSets'
        UPDATE_LANGUAGE_PACK_STRINGS = 'updateLanguagePackStrings'
        UPDATE_MESSAGE_CONTENT = 'updateMessageContent'
        UPDATE_MESSAGE_CONTENT_OPENED = 'updateMessageContentOpened'
        UPDATE_MESSAGE_EDITED = 'updateMessageEdited'
        UPDATE_MESSAGE_INTERACTION_INFO = 'updateMessageInteractionInfo'
        UPDATE_MESSAGE_IS_PINNED = 'updateMessageIsPinned'
        UPDATE_MESSAGE_LIVE_LOCATION_VIEWED = 'updateMessageLiveLocationViewed'
        UPDATE_MESSAGE_MENTION_READ = 'updateMessageMentionRead'
        UPDATE_MESSAGE_SEND_ACKNOWLEDGED = 'updateMessageSendAcknowledged'
        UPDATE_MESSAGE_SEND_FAILED = 'updateMessageSendFailed'
        UPDATE_MESSAGE_SEND_SUCCEEDED = 'updateMessageSendSucceeded'
        UPDATE_MESSAGE_UNREAD_REACTIONS = 'updateMessageUnreadReactions'
        UPDATE_NEW_CALL_SIGNALING_DATA = 'updateNewCallSignalingData'
        UPDATE_NEW_CALLBACK_QUERY = 'updateNewCallbackQuery'
        UPDATE_NEW_CHAT = 'updateNewChat'
        UPDATE_NEW_CHAT_JOIN_REQUEST = 'updateNewChatJoinRequest'
        UPDATE_NEW_CHOSEN_INLINE_RESULT = 'updateNewChosenInlineResult'
        UPDATE_NEW_CUSTOM_EVENT = 'updateNewCustomEvent'
        UPDATE_NEW_CUSTOM_QUERY = 'updateNewCustomQuery'
        UPDATE_NEW_INLINE_CALLBACK_QUERY = 'updateNewInlineCallbackQuery'
        UPDATE_NEW_INLINE_QUERY = 'updateNewInlineQuery'
        UPDATE_NEW_MESSAGE = 'updateNewMessage'
        UPDATE_NEW_PRE_CHECKOUT_QUERY = 'updateNewPreCheckoutQuery'
        UPDATE_NEW_SHIPPING_QUERY = 'updateNewShippingQuery'
        UPDATE_NOTIFICATION = 'updateNotification'
        UPDATE_NOTIFICATION_GROUP = 'updateNotificationGroup'
        UPDATE_OPTION = 'updateOption'
        UPDATE_POLL = 'updatePoll'
        UPDATE_POLL_ANSWER = 'updatePollAnswer'
        UPDATE_REACTIONS = 'updateReactions'
        UPDATE_RECENT_STICKERS = 'updateRecentStickers'
        UPDATE_SAVED_ANIMATIONS = 'updateSavedAnimations'
        UPDATE_SAVED_NOTIFICATION_SOUNDS = 'updateSavedNotificationSounds'
        UPDATE_SCOPE_NOTIFICATION_SETTINGS = 'updateScopeNotificationSettings'
        UPDATE_SECRET_CHAT = 'updateSecretChat'
        UPDATE_SELECTED_BACKGROUND = 'updateSelectedBackground'
        UPDATE_SERVICE_NOTIFICATION = 'updateServiceNotification'
        UPDATE_STICKER_SET = 'updateStickerSet'
        UPDATE_SUGGESTED_ACTIONS = 'updateSuggestedActions'
        UPDATE_SUPERGROUP = 'updateSupergroup'
        UPDATE_SUPERGROUP_FULL_INFO = 'updateSupergroupFullInfo'
        UPDATE_TERMS_OF_SERVICE = 'updateTermsOfService'
        UPDATE_TRENDING_STICKER_SETS = 'updateTrendingStickerSets'
        UPDATE_UNREAD_CHAT_COUNT = 'updateUnreadChatCount'
        UPDATE_UNREAD_MESSAGE_COUNT = 'updateUnreadMessageCount'
        UPDATE_USER = 'updateUser'
        UPDATE_USER_FULL_INFO = 'updateUserFullInfo'
        UPDATE_USER_PRIVACY_SETTING_RULES = 'updateUserPrivacySettingRules'
        UPDATE_USER_STATUS = 'updateUserStatus'
        UPDATE_USERS_NEARBY = 'updateUsersNearby'
        UPDATE_WEB_APP_MESSAGE_SENT = 'updateWebAppMessageSent'
        UPDATES = 'updates'
        UPGRADE_BASIC_GROUP_CHAT_TO_SUPERGROUP_CHAT = 'upgradeBasicGroupChatToSupergroupChat'
        UPLOAD_FILE = 'uploadFile'
        UPLOAD_STICKER_FILE = 'uploadStickerFile'
        USER = 'user'
        USER_FULL_INFO = 'userFullInfo'
        USER_PRIVACY_SETTING = 'userPrivacySetting'
        USER_PRIVACY_SETTING_ALLOW_CALLS = 'userPrivacySettingAllowCalls'
        USER_PRIVACY_SETTING_ALLOW_CHAT_INVITES = 'userPrivacySettingAllowChatInvites'
        USER_PRIVACY_SETTING_ALLOW_FINDING_BY_PHONE_NUMBER = 'userPrivacySettingAllowFindingByPhoneNumber'
        USER_PRIVACY_SETTING_ALLOW_PEER_TO_PEER_CALLS = 'userPrivacySettingAllowPeerToPeerCalls'
        USER_PRIVACY_SETTING_SHOW_LINK_IN_FORWARDED_MESSAGES = 'userPrivacySettingShowLinkInForwardedMessages'
        USER_PRIVACY_SETTING_SHOW_PHONE_NUMBER = 'userPrivacySettingShowPhoneNumber'
        USER_PRIVACY_SETTING_SHOW_PROFILE_PHOTO = 'userPrivacySettingShowProfilePhoto'
        USER_PRIVACY_SETTING_SHOW_STATUS = 'userPrivacySettingShowStatus'
        USER_PRIVACY_SETTING_RULE = 'userPrivacySettingRule'
        USER_PRIVACY_SETTING_RULE_ALLOW_ALL = 'userPrivacySettingRuleAllowAll'
        USER_PRIVACY_SETTING_RULE_ALLOW_CHAT_MEMBERS = 'userPrivacySettingRuleAllowChatMembers'
        USER_PRIVACY_SETTING_RULE_ALLOW_CONTACTS = 'userPrivacySettingRuleAllowContacts'
        USER_PRIVACY_SETTING_RULE_ALLOW_USERS = 'userPrivacySettingRuleAllowUsers'
        USER_PRIVACY_SETTING_RULE_RESTRICT_ALL = 'userPrivacySettingRuleRestrictAll'
        USER_PRIVACY_SETTING_RULE_RESTRICT_CHAT_MEMBERS = 'userPrivacySettingRuleRestrictChatMembers'
        USER_PRIVACY_SETTING_RULE_RESTRICT_CONTACTS = 'userPrivacySettingRuleRestrictContacts'
        USER_PRIVACY_SETTING_RULE_RESTRICT_USERS = 'userPrivacySettingRuleRestrictUsers'
        USER_PRIVACY_SETTING_RULES = 'userPrivacySettingRules'
        USER_STATUS = 'userStatus'
        USER_STATUS_EMPTY = 'userStatusEmpty'
        USER_STATUS_LAST_MONTH = 'userStatusLastMonth'
        USER_STATUS_LAST_WEEK = 'userStatusLastWeek'
        USER_STATUS_OFFLINE = 'userStatusOffline'
        USER_STATUS_ONLINE = 'userStatusOnline'
        USER_STATUS_RECENTLY = 'userStatusRecently'
        USER_TYPE = 'userType'
        USER_TYPE_BOT = 'userTypeBot'
        USER_TYPE_DELETED = 'userTypeDeleted'
        USER_TYPE_REGULAR = 'userTypeRegular'
        USER_TYPE_UNKNOWN = 'userTypeUnknown'
        USERS = 'users'
        VALIDATE_ORDER_INFO = 'validateOrderInfo'
        VALIDATED_ORDER_INFO = 'validatedOrderInfo'
        VECTOR_PATH_COMMAND = 'vectorPathCommand'
        VECTOR_PATH_COMMAND_CUBIC_BEZIER_CURVE = 'vectorPathCommandCubicBezierCurve'
        VECTOR_PATH_COMMAND_LINE = 'vectorPathCommandLine'
        VENUE = 'venue'
        VIDEO = 'video'
        VIDEO_CHAT = 'videoChat'
        VIDEO_NOTE = 'videoNote'
        VIEW_MESSAGES = 'viewMessages'
        VIEW_TRENDING_STICKER_SETS = 'viewTrendingStickerSets'
        VOICE_NOTE = 'voiceNote'
        WEB_APP_INFO = 'webAppInfo'
        WEB_PAGE = 'webPage'
        WEB_PAGE_INSTANT_VIEW = 'webPageInstantView'
        WRITE_GENERATED_FILE_PART = 'writeGeneratedFilePart'

    def __init__(self, client: 'Client'):
        self.client = client

    async def accept_call(
            self,
            call_id: int,
            protocol: CallProtocol,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Accepts an incoming call
        
        :param call_id: Call identifier
        :type call_id: :class:`int`
        
        :param protocol: The call protocols supported by the application
        :type protocol: :class:`CallProtocol`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AcceptCall.construct if skip_validation else AcceptCall

        return await self.client.request(
            _constructor(
                call_id=call_id,
                protocol=protocol,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def accept_terms_of_service(
            self,
            terms_of_service_id: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Accepts Telegram terms of services
        
        :param terms_of_service_id: Terms of service identifier
        :type terms_of_service_id: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AcceptTermsOfService.construct if skip_validation else AcceptTermsOfService

        return await self.client.request(
            _constructor(
                terms_of_service_id=terms_of_service_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_chat_member(
            self,
            chat_id: int,
            user_id: int,
            forward_limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds a new member to a chat. Members can't be added to private or secret chats
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param user_id: Identifier of the user
        :type user_id: :class:`int`
        
        :param forward_limit: The number of earlier messages from the chat to be forwarded to the new member; up to 100. Ignored for supergroups and channels, or if the added user is a bot
        :type forward_limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AddChatMember.construct if skip_validation else AddChatMember

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                user_id=user_id,
                forward_limit=forward_limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_chat_members(
            self,
            chat_id: int,
            user_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds multiple new members to a chat. Currently, this method is only available for supergroups and channels. This method can't be used to join a chat. Members can't be added to a channel if it has more than 200 members
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param user_ids: Identifiers of the users to be added to the chat. The maximum number of added users is 20 for supergroups and 100 for channels
        :type user_ids: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AddChatMembers.construct if skip_validation else AddChatMembers

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                user_ids=user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_chat_to_list(
            self,
            chat_id: int,
            chat_list: ChatList,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds a chat to a chat list. A chat can't be simultaneously in Main and Archive chat lists, so it is automatically removed from another one if needed
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param chat_list: The chat list. Use getChatListsToAddChat to get suitable chat lists
        :type chat_list: :class:`ChatList`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AddChatToList.construct if skip_validation else AddChatToList

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                chat_list=chat_list,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_contact(
            self,
            contact: Contact,
            share_phone_number: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds a user to the contact list or edits an existing contact by their user identifier
        
        :param contact: The contact to add or edit; phone number may be empty and needs to be specified only if known, vCard is ignored
        :type contact: :class:`Contact`
        
        :param share_phone_number: Pass true to share the current user's phone number with the new contact. A corresponding rule to userPrivacySettingShowPhoneNumber will be added if needed. Use the field userFullInfo.need_phone_number_privacy_exception to check whether the current user needs to be asked to share their phone number
        :type share_phone_number: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AddContact.construct if skip_validation else AddContact

        return await self.client.request(
            _constructor(
                contact=contact,
                share_phone_number=share_phone_number,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_custom_server_language_pack(
            self,
            language_pack_id: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds a custom server language pack to the list of installed language packs in current localization target. Can be called before authorization
        
        :param language_pack_id: Identifier of a language pack to be added; may be different from a name that is used in an "https://t.me/setlanguage/" link
        :type language_pack_id: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AddCustomServerLanguagePack.construct if skip_validation else AddCustomServerLanguagePack

        return await self.client.request(
            _constructor(
                language_pack_id=language_pack_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_favorite_sticker(
            self,
            sticker: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds a new sticker to the list of favorite stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set can be added to this list
        
        :param sticker: Sticker file to add
        :type sticker: :class:`InputFile`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AddFavoriteSticker.construct if skip_validation else AddFavoriteSticker

        return await self.client.request(
            _constructor(
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_file_to_downloads(
            self,
            file_id: int,
            chat_id: int,
            message_id: int,
            priority: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> File:
        """
        Adds a file from a message to the list of file downloads. Download progress and completion of the download will be notified through updateFile updates. If message database is used, the list of file downloads is persistent across application restarts. The downloading is independent from download using downloadFile, i.e. it continues if downloadFile is canceled or is used to download a part of the file
        
        :param file_id: Identifier of the file to download
        :type file_id: :class:`int`
        
        :param chat_id: Chat identifier of the message with the file
        :type chat_id: :class:`int`
        
        :param message_id: Message identifier
        :type message_id: :class:`int`
        
        :param priority: Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first
        :type priority: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.File`
        """
        _constructor = AddFileToDownloads.construct if skip_validation else AddFileToDownloads

        return await self.client.request(
            _constructor(
                file_id=file_id,
                chat_id=chat_id,
                message_id=message_id,
                priority=priority,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_local_message(
            self,
            chat_id: int,
            sender_id: MessageSender,
            reply_to_message_id: int,
            disable_notification: bool,
            input_message_content: InputMessageContent,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Adds a local message to a chat. The message is persistent across application restarts only if the message database is used. Returns the added message
        
        :param chat_id: Target chat
        :type chat_id: :class:`int`
        
        :param sender_id: Identifier of the sender of the message
        :type sender_id: :class:`MessageSender`
        
        :param reply_to_message_id: Identifier of the replied message; 0 if none
        :type reply_to_message_id: :class:`int`
        
        :param disable_notification: Pass true to disable notification for the message
        :type disable_notification: :class:`bool`
        
        :param input_message_content: The content of the message to be added
        :type input_message_content: :class:`InputMessageContent`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = AddLocalMessage.construct if skip_validation else AddLocalMessage

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                sender_id=sender_id,
                reply_to_message_id=reply_to_message_id,
                disable_notification=disable_notification,
                input_message_content=input_message_content,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_log_message(
            self,
            verbosity_level: int,
            text: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds a message to TDLib internal log. Can be called synchronously
        
        :param verbosity_level: The minimum verbosity level needed for the message to be logged; 0-1023
        :type verbosity_level: :class:`int`
        
        :param text: Text of a message to log
        :type text: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AddLogMessage.construct if skip_validation else AddLogMessage

        return await self.client.request(
            _constructor(
                verbosity_level=verbosity_level,
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_network_statistics(
            self,
            entry: NetworkStatisticsEntry,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds the specified data to data usage statistics. Can be called before authorization
        
        :param entry: The network statistics entry with the data to be added to statistics
        :type entry: :class:`NetworkStatisticsEntry`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AddNetworkStatistics.construct if skip_validation else AddNetworkStatistics

        return await self.client.request(
            _constructor(
                entry=entry,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_proxy(
            self,
            server: str,
            port: int,
            enable: bool,
            type_: ProxyType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Proxy:
        """
        Adds a proxy server for network requests. Can be called before authorization
        
        :param server: Proxy server IP address
        :type server: :class:`str`
        
        :param port: Proxy server port
        :type port: :class:`int`
        
        :param enable: Pass true to immediately enable the proxy
        :type enable: :class:`bool`
        
        :param type_: Proxy type
        :type type_: :class:`ProxyType`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Proxy`
        """
        _constructor = AddProxy.construct if skip_validation else AddProxy

        return await self.client.request(
            _constructor(
                server=server,
                port=port,
                enable=enable,
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_recent_sticker(
            self,
            is_attached: bool,
            sticker: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Stickers:
        """
        Manually adds a new sticker to the list of recently used stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set can be added to this list
        
        :param is_attached: Pass true to add the sticker to the list of stickers recently attached to photo or video files; pass false to add the sticker to the list of recently sent stickers
        :type is_attached: :class:`bool`
        
        :param sticker: Sticker file to add
        :type sticker: :class:`InputFile`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Stickers`
        """
        _constructor = AddRecentSticker.construct if skip_validation else AddRecentSticker

        return await self.client.request(
            _constructor(
                is_attached=is_attached,
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_recently_found_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds a chat to the list of recently found chats. The chat is added to the beginning of the list. If the chat is already in the list, it will be removed from the list first
        
        :param chat_id: Identifier of the chat to add
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AddRecentlyFoundChat.construct if skip_validation else AddRecentlyFoundChat

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_saved_animation(
            self,
            animation: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Manually adds a new animation to the list of saved animations. The new animation is added to the beginning of the list. If the animation was already in the list, it is removed first. Only non-secret video animations with MIME type "video/mp4" can be added to the list
        
        :param animation: The animation file to be added. Only animations known to the server (i.e., successfully sent via a message) can be added to the list
        :type animation: :class:`InputFile`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AddSavedAnimation.construct if skip_validation else AddSavedAnimation

        return await self.client.request(
            _constructor(
                animation=animation,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_saved_notification_sound(
            self,
            sound: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> NotificationSound:
        """
        Adds a new notification sound to the list of saved notification sounds. The new notification sound is added to the top of the list. If it is already in the list, it is position isn't changed
        
        :param sound: Notification sound file to add
        :type sound: :class:`InputFile`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.NotificationSound`
        """
        _constructor = AddSavedNotificationSound.construct if skip_validation else AddSavedNotificationSound

        return await self.client.request(
            _constructor(
                sound=sound,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_sticker_to_set(
            self,
            user_id: int,
            name: str,
            sticker: InputSticker,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSet:
        """
        Adds a new sticker to a set; for bots only. Returns the sticker set
        
        :param user_id: Sticker set owner
        :type user_id: :class:`int`
        
        :param name: Sticker set name
        :type name: :class:`str`
        
        :param sticker: Sticker to add to the set
        :type sticker: :class:`InputSticker`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSet`
        """
        _constructor = AddStickerToSet.construct if skip_validation else AddStickerToSet

        return await self.client.request(
            _constructor(
                user_id=user_id,
                name=name,
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def answer_callback_query(
            self,
            callback_query_id: int,
            text: str,
            show_alert: bool,
            url: str,
            cache_time: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the result of a callback query; for bots only
        
        :param callback_query_id: Identifier of the callback query
        :type callback_query_id: :class:`int`
        
        :param text: Text of the answer
        :type text: :class:`str`
        
        :param show_alert: Pass true to show an alert to the user instead of a toast notification
        :type show_alert: :class:`bool`
        
        :param url: URL to be opened
        :type url: :class:`str`
        
        :param cache_time: Time during which the result of the query can be cached, in seconds
        :type cache_time: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AnswerCallbackQuery.construct if skip_validation else AnswerCallbackQuery

        return await self.client.request(
            _constructor(
                callback_query_id=callback_query_id,
                text=text,
                show_alert=show_alert,
                url=url,
                cache_time=cache_time,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def answer_custom_query(
            self,
            custom_query_id: int,
            data: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Answers a custom query; for bots only
        
        :param custom_query_id: Identifier of a custom query
        :type custom_query_id: :class:`int`
        
        :param data: JSON-serialized answer to the query
        :type data: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AnswerCustomQuery.construct if skip_validation else AnswerCustomQuery

        return await self.client.request(
            _constructor(
                custom_query_id=custom_query_id,
                data=data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def answer_inline_query(
            self,
            inline_query_id: int,
            is_personal: bool,
            results: list[InputInlineQueryResult],
            cache_time: int,
            next_offset: str,
            switch_pm_text: str,
            switch_pm_parameter: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the result of an inline query; for bots only
        
        :param inline_query_id: Identifier of the inline query
        :type inline_query_id: :class:`int`
        
        :param is_personal: Pass true if results may be cached and returned only for the user that sent the query. By default, results may be returned to any user who sends the same query
        :type is_personal: :class:`bool`
        
        :param results: The results of the query
        :type results: :class:`list[InputInlineQueryResult]`
        
        :param cache_time: Allowed time to cache the results of the query, in seconds
        :type cache_time: :class:`int`
        
        :param next_offset: Offset for the next inline query; pass an empty string if there are no more results
        :type next_offset: :class:`str`
        
        :param switch_pm_text: If non-empty, this text must be shown on the button that opens a private chat with the bot and sends a start message to the bot with the parameter switch_pm_parameter
        :type switch_pm_text: :class:`str`
        
        :param switch_pm_parameter: The parameter for the bot start message
        :type switch_pm_parameter: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AnswerInlineQuery.construct if skip_validation else AnswerInlineQuery

        return await self.client.request(
            _constructor(
                inline_query_id=inline_query_id,
                is_personal=is_personal,
                results=results,
                cache_time=cache_time,
                next_offset=next_offset,
                switch_pm_text=switch_pm_text,
                switch_pm_parameter=switch_pm_parameter,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def answer_pre_checkout_query(
            self,
            pre_checkout_query_id: int,
            error_message: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the result of a pre-checkout query; for bots only
        
        :param pre_checkout_query_id: Identifier of the pre-checkout query
        :type pre_checkout_query_id: :class:`int`
        
        :param error_message: An error message, empty on success
        :type error_message: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AnswerPreCheckoutQuery.construct if skip_validation else AnswerPreCheckoutQuery

        return await self.client.request(
            _constructor(
                pre_checkout_query_id=pre_checkout_query_id,
                error_message=error_message,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def answer_shipping_query(
            self,
            shipping_query_id: int,
            shipping_options: list[ShippingOption],
            error_message: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the result of a shipping query; for bots only
        
        :param shipping_query_id: Identifier of the shipping query
        :type shipping_query_id: :class:`int`
        
        :param shipping_options: Available shipping options
        :type shipping_options: :class:`list[ShippingOption]`
        
        :param error_message: An error message, empty on success
        :type error_message: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = AnswerShippingQuery.construct if skip_validation else AnswerShippingQuery

        return await self.client.request(
            _constructor(
                shipping_query_id=shipping_query_id,
                shipping_options=shipping_options,
                error_message=error_message,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def answer_web_app_query(
            self,
            web_app_query_id: str,
            result: InputInlineQueryResult,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> SentWebAppMessage:
        """
        Sets the result of interaction with a web app and sends corresponding message on behalf of the user to the chat from which the query originated; for bots only
        
        :param web_app_query_id: Identifier of the web app query
        :type web_app_query_id: :class:`str`
        
        :param result: The result of the query
        :type result: :class:`InputInlineQueryResult`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.SentWebAppMessage`
        """
        _constructor = AnswerWebAppQuery.construct if skip_validation else AnswerWebAppQuery

        return await self.client.request(
            _constructor(
                web_app_query_id=web_app_query_id,
                result=result,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def ban_chat_member(
            self,
            chat_id: int,
            member_id: MessageSender,
            banned_until_date: int,
            revoke_messages: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Bans a member in a chat. Members can't be banned in private or secret chats. In supergroups and channels, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param member_id: Member identifier
        :type member_id: :class:`MessageSender`
        
        :param banned_until_date: Point in time (Unix timestamp) when the user will be unbanned; 0 if never. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever. Ignored in basic groups and if a chat is banned
        :type banned_until_date: :class:`int`
        
        :param revoke_messages: Pass true to delete all messages in the chat for the user that is being removed. Always true for supergroups and channels
        :type revoke_messages: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = BanChatMember.construct if skip_validation else BanChatMember

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                member_id=member_id,
                banned_until_date=banned_until_date,
                revoke_messages=revoke_messages,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def block_message_sender_from_replies(
            self,
            message_id: int,
            delete_message: bool,
            delete_all_messages: bool,
            report_spam: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Blocks an original sender of a message in the Replies chat
        
        :param message_id: The identifier of an incoming message in the Replies chat
        :type message_id: :class:`int`
        
        :param delete_message: Pass true to delete the message
        :type delete_message: :class:`bool`
        
        :param delete_all_messages: Pass true to delete all messages from the same sender
        :type delete_all_messages: :class:`bool`
        
        :param report_spam: Pass true to report the sender to the Telegram moderators
        :type report_spam: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = BlockMessageSenderFromReplies.construct if skip_validation else BlockMessageSenderFromReplies

        return await self.client.request(
            _constructor(
                message_id=message_id,
                delete_message=delete_message,
                delete_all_messages=delete_all_messages,
                report_spam=report_spam,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def can_transfer_ownership(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> CanTransferOwnershipResult:
        """
        Checks whether the current session can be used to transfer a chat ownership to another user
        
        """
        return await self.client.request(
            CanTransferOwnership(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def cancel_download_file(
            self,
            file_id: int,
            only_if_pending: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Stops the downloading of a file. If a file has already been downloaded, does nothing
        
        :param file_id: Identifier of a file to stop downloading
        :type file_id: :class:`int`
        
        :param only_if_pending: Pass true to stop downloading only if it hasn't been started, i.e. request hasn't been sent to server
        :type only_if_pending: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CancelDownloadFile.construct if skip_validation else CancelDownloadFile

        return await self.client.request(
            _constructor(
                file_id=file_id,
                only_if_pending=only_if_pending,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def cancel_password_reset(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Cancels reset of 2-step verification password. The method can be called if passwordState.pending_reset_date > 0
        
        """
        return await self.client.request(
            CancelPasswordReset(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def cancel_upload_file(
            self,
            file_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Stops the uploading of a file. Supported only for files uploaded by using uploadFile. For other files the behavior is undefined
        
        :param file_id: Identifier of the file to stop uploading
        :type file_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CancelUploadFile.construct if skip_validation else CancelUploadFile

        return await self.client.request(
            _constructor(
                file_id=file_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def change_imported_contacts(
            self,
            contacts: list[Contact],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ImportedContacts:
        """
        Changes imported contacts using the list of contacts saved on the device. Imports newly added contacts and, if at least the file database is enabled, deletes recently deleted contacts. Query result depends on the result of the previous query, so only one query is possible at the same time
        
        :param contacts: The new list of contacts, contact's vCard are ignored and are not imported
        :type contacts: :class:`list[Contact]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ImportedContacts`
        """
        _constructor = ChangeImportedContacts.construct if skip_validation else ChangeImportedContacts

        return await self.client.request(
            _constructor(
                contacts=contacts,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def change_phone_number(
            self,
            phone_number: str,
            settings: PhoneNumberAuthenticationSettings,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> AuthenticationCodeInfo:
        """
        Changes the phone number of the user and sends an authentication code to the user's new phone number. On success, returns information about the sent code
        
        :param phone_number: The new phone number of the user in international format
        :type phone_number: :class:`str`
        
        :param settings: Settings for the authentication of the user's phone number; pass null to use default settings
        :type settings: :class:`PhoneNumberAuthenticationSettings`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AuthenticationCodeInfo`
        """
        _constructor = ChangePhoneNumber.construct if skip_validation else ChangePhoneNumber

        return await self.client.request(
            _constructor(
                phone_number=phone_number,
                settings=settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def change_sticker_set(
            self,
            set_id: int,
            is_installed: bool,
            is_archived: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Installs/uninstalls or activates/archives a sticker set
        
        :param set_id: Identifier of the sticker set
        :type set_id: :class:`int`
        
        :param is_installed: The new value of is_installed
        :type is_installed: :class:`bool`
        
        :param is_archived: The new value of is_archived. A sticker set can't be installed and archived simultaneously
        :type is_archived: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ChangeStickerSet.construct if skip_validation else ChangeStickerSet

        return await self.client.request(
            _constructor(
                set_id=set_id,
                is_installed=is_installed,
                is_archived=is_archived,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_authentication_bot_token(
            self,
            token: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks the authentication token of a bot; to log in as a bot. Works only when the current authorization state is authorizationStateWaitPhoneNumber. Can be used instead of setAuthenticationPhoneNumber and checkAuthenticationCode to log in
        
        :param token: The bot token
        :type token: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CheckAuthenticationBotToken.construct if skip_validation else CheckAuthenticationBotToken

        return await self.client.request(
            _constructor(
                token=token,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_authentication_code(
            self,
            code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks the authentication code. Works only when the current authorization state is authorizationStateWaitCode
        
        :param code: Authentication code to check
        :type code: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CheckAuthenticationCode.construct if skip_validation else CheckAuthenticationCode

        return await self.client.request(
            _constructor(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_authentication_password(
            self,
            password: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks the authentication password for correctness. Works only when the current authorization state is authorizationStateWaitPassword
        
        :param password: The password to check
        :type password: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CheckAuthenticationPassword.construct if skip_validation else CheckAuthenticationPassword

        return await self.client.request(
            _constructor(
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_authentication_password_recovery_code(
            self,
            recovery_code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks whether a password recovery code sent to an email address is valid. Works only when the current authorization state is authorizationStateWaitPassword
        
        :param recovery_code: Recovery code to check
        :type recovery_code: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CheckAuthenticationPasswordRecoveryCode.construct if skip_validation else CheckAuthenticationPasswordRecoveryCode

        return await self.client.request(
            _constructor(
                recovery_code=recovery_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_change_phone_number_code(
            self,
            code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks the authentication code sent to confirm a new phone number of the user
        
        :param code: Authentication code to check
        :type code: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CheckChangePhoneNumberCode.construct if skip_validation else CheckChangePhoneNumberCode

        return await self.client.request(
            _constructor(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_chat_invite_link(
            self,
            invite_link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLinkInfo:
        """
        Checks the validity of an invite link for a chat and returns information about the corresponding chat
        
        :param invite_link: Invite link to be checked
        :type invite_link: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLinkInfo`
        """
        _constructor = CheckChatInviteLink.construct if skip_validation else CheckChatInviteLink

        return await self.client.request(
            _constructor(
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_chat_username(
            self,
            chat_id: int,
            username: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> CheckChatUsernameResult:
        """
        Checks whether a username can be set for a chat
        
        :param chat_id: Chat identifier; must be identifier of a supergroup chat, or a channel chat, or a private chat with self, or zero if the chat is being created
        :type chat_id: :class:`int`
        
        :param username: Username to be checked
        :type username: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.CheckChatUsernameResult`
        """
        _constructor = CheckChatUsername.construct if skip_validation else CheckChatUsername

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                username=username,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_created_public_chats_limit(
            self,
            type_: PublicChatType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks whether the maximum number of owned public chats has been reached. Returns corresponding error if the limit was reached
        
        :param type_: Type of the public chats, for which to check the limit
        :type type_: :class:`PublicChatType`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CheckCreatedPublicChatsLimit.construct if skip_validation else CheckCreatedPublicChatsLimit

        return await self.client.request(
            _constructor(
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_database_encryption_key(
            self,
            encryption_key: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks the database encryption key for correctness. Works only when the current authorization state is authorizationStateWaitEncryptionKey
        
        :param encryption_key: Encryption key to check or set up
        :type encryption_key: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CheckDatabaseEncryptionKey.construct if skip_validation else CheckDatabaseEncryptionKey

        return await self.client.request(
            _constructor(
                encryption_key=encryption_key,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_email_address_verification_code(
            self,
            code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks the email address verification code for Telegram Passport
        
        :param code: Verification code to check
        :type code: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CheckEmailAddressVerificationCode.construct if skip_validation else CheckEmailAddressVerificationCode

        return await self.client.request(
            _constructor(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_password_recovery_code(
            self,
            recovery_code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks whether a 2-step verification password recovery code sent to an email address is valid
        
        :param recovery_code: Recovery code to check
        :type recovery_code: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CheckPasswordRecoveryCode.construct if skip_validation else CheckPasswordRecoveryCode

        return await self.client.request(
            _constructor(
                recovery_code=recovery_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_phone_number_confirmation_code(
            self,
            code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks phone number confirmation code
        
        :param code: Confirmation code to check
        :type code: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CheckPhoneNumberConfirmationCode.construct if skip_validation else CheckPhoneNumberConfirmationCode

        return await self.client.request(
            _constructor(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_phone_number_verification_code(
            self,
            code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks the phone number verification code for Telegram Passport
        
        :param code: Verification code to check
        :type code: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CheckPhoneNumberVerificationCode.construct if skip_validation else CheckPhoneNumberVerificationCode

        return await self.client.request(
            _constructor(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_recovery_email_address_code(
            self,
            code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PasswordState:
        """
        Checks the 2-step verification recovery email address verification code
        
        :param code: Verification code to check
        :type code: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PasswordState`
        """
        _constructor = CheckRecoveryEmailAddressCode.construct if skip_validation else CheckRecoveryEmailAddressCode

        return await self.client.request(
            _constructor(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_sticker_set_name(
            self,
            name: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> CheckStickerSetNameResult:
        """
        Checks whether a name can be used for a new sticker set
        
        :param name: Name to be checked
        :type name: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.CheckStickerSetNameResult`
        """
        _constructor = CheckStickerSetName.construct if skip_validation else CheckStickerSetName

        return await self.client.request(
            _constructor(
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def clean_file_name(
            self,
            file_name: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Removes potentially dangerous characters from the name of a file. The encoding of the file name is supposed to be UTF-8. Returns an empty string on failure. Can be called synchronously
        
        :param file_name: File name or path to the file
        :type file_name: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """
        _constructor = CleanFileName.construct if skip_validation else CleanFileName

        return await self.client.request(
            _constructor(
                file_name=file_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def clear_all_draft_messages(
            self,
            exclude_secret_chats: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Clears message drafts in all chats
        
        :param exclude_secret_chats: Pass true to keep local message drafts in secret chats
        :type exclude_secret_chats: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ClearAllDraftMessages.construct if skip_validation else ClearAllDraftMessages

        return await self.client.request(
            _constructor(
                exclude_secret_chats=exclude_secret_chats,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def clear_imported_contacts(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Clears all imported contacts, contact list remains unchanged
        
        """
        return await self.client.request(
            ClearImportedContacts(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def clear_recent_stickers(
            self,
            is_attached: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Clears the list of recently used stickers
        
        :param is_attached: Pass true to clear the list of stickers recently attached to photo or video files; pass false to clear the list of recently sent stickers
        :type is_attached: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ClearRecentStickers.construct if skip_validation else ClearRecentStickers

        return await self.client.request(
            _constructor(
                is_attached=is_attached,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def clear_recently_found_chats(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Clears the list of recently found chats
        
        """
        return await self.client.request(
            ClearRecentlyFoundChats(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def click_animated_emoji_message(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Sticker:
        """
        Informs TDLib that a message with an animated emoji was clicked by the user. Returns a big animated sticker to be played or a 404 error if usual animation needs to be played
        
        :param chat_id: Chat identifier of the message
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the clicked message
        :type message_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Sticker`
        """
        _constructor = ClickAnimatedEmojiMessage.construct if skip_validation else ClickAnimatedEmojiMessage

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def close(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Closes the TDLib instance. All databases will be flushed to disk and properly closed. After the close completes, updateAuthorizationState with authorizationStateClosed will be sent. Can be called before initialization
        
        """
        return await self.client.request(
            Close(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def close_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs TDLib that the chat is closed by the user. Many useful activities depend on the chat being opened or closed
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CloseChat.construct if skip_validation else CloseChat

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def close_secret_chat(
            self,
            secret_chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Closes a secret chat, effectively transferring its state to secretChatStateClosed
        
        :param secret_chat_id: Secret chat identifier
        :type secret_chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CloseSecretChat.construct if skip_validation else CloseSecretChat

        return await self.client.request(
            _constructor(
                secret_chat_id=secret_chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def close_web_app(
            self,
            web_app_launch_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs TDLib that a previously opened web app was closed
        
        :param web_app_launch_id: Identifier of web app launch, received from openWebApp
        :type web_app_launch_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = CloseWebApp.construct if skip_validation else CloseWebApp

        return await self.client.request(
            _constructor(
                web_app_launch_id=web_app_launch_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def confirm_qr_code_authentication(
            self,
            link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Session:
        """
        Confirms QR code authentication on another device. Returns created session on success
        
        :param link: A link from a QR code. The link must be scanned by the in-app camera
        :type link: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Session`
        """
        _constructor = ConfirmQrCodeAuthentication.construct if skip_validation else ConfirmQrCodeAuthentication

        return await self.client.request(
            _constructor(
                link=link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_basic_group_chat(
            self,
            basic_group_id: int,
            force: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Returns an existing chat corresponding to a known basic group
        
        :param basic_group_id: Basic group identifier
        :type basic_group_id: :class:`int`
        
        :param force: Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect
        :type force: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """
        _constructor = CreateBasicGroupChat.construct if skip_validation else CreateBasicGroupChat

        return await self.client.request(
            _constructor(
                basic_group_id=basic_group_id,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_call(
            self,
            user_id: int,
            protocol: CallProtocol,
            is_video: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> CallId:
        """
        Creates a new call
        
        :param user_id: Identifier of the user to be called
        :type user_id: :class:`int`
        
        :param protocol: The call protocols supported by the application
        :type protocol: :class:`CallProtocol`
        
        :param is_video: Pass true to create a video call
        :type is_video: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.CallId`
        """
        _constructor = CreateCall.construct if skip_validation else CreateCall

        return await self.client.request(
            _constructor(
                user_id=user_id,
                protocol=protocol,
                is_video=is_video,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_chat_filter(
            self,
            filter_: ChatFilter,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatFilterInfo:
        """
        Creates new chat filter. Returns information about the created chat filter
        
        :param filter_: Chat filter
        :type filter_: :class:`ChatFilter`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatFilterInfo`
        """
        _constructor = CreateChatFilter.construct if skip_validation else CreateChatFilter

        return await self.client.request(
            _constructor(
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_chat_invite_link(
            self,
            chat_id: int,
            name: typing.Optional[str],
            expiration_date: int,
            member_limit: int,
            creates_join_request: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLink:
        """
        Creates a new invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param name: Invite link name; 0-32 characters, defaults to None
        :type name: :class:`str`, optional
        
        :param expiration_date: Point in time (Unix timestamp) when the link will expire; pass 0 if never
        :type expiration_date: :class:`int`
        
        :param member_limit: The maximum number of chat members that can join the chat via the link simultaneously; 0-99999; pass 0 if not limited
        :type member_limit: :class:`int`
        
        :param creates_join_request: Pass true if users joining the chat via the link need to be approved by chat administrators. In this case, member_limit must be 0
        :type creates_join_request: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLink`
        """
        _constructor = CreateChatInviteLink.construct if skip_validation else CreateChatInviteLink

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                name=name,
                expiration_date=expiration_date,
                member_limit=member_limit,
                creates_join_request=creates_join_request,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_new_basic_group_chat(
            self,
            user_ids: list[int],
            title: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Creates a new basic group and sends a corresponding messageBasicGroupChatCreate. Returns the newly created chat
        
        :param user_ids: Identifiers of users to be added to the basic group
        :type user_ids: :class:`list[int]`
        
        :param title: Title of the new basic group; 1-128 characters
        :type title: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """
        _constructor = CreateNewBasicGroupChat.construct if skip_validation else CreateNewBasicGroupChat

        return await self.client.request(
            _constructor(
                user_ids=user_ids,
                title=title,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_new_secret_chat(
            self,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Creates a new secret chat. Returns the newly created chat
        
        :param user_id: Identifier of the target user
        :type user_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """
        _constructor = CreateNewSecretChat.construct if skip_validation else CreateNewSecretChat

        return await self.client.request(
            _constructor(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_new_sticker_set(
            self,
            user_id: int,
            title: str,
            name: str,
            stickers: list[InputSticker],
            source: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSet:
        """
        Creates a new sticker set. Returns the newly created sticker set
        
        :param user_id: Sticker set owner; ignored for regular users
        :type user_id: :class:`int`
        
        :param title: Sticker set title; 1-64 characters
        :type title: :class:`str`
        
        :param name: Sticker set name. Can contain only English letters, digits and underscores. Must end with *"_by_<bot username>"* (*<bot_username>* is case insensitive) for bots; 1-64 characters
        :type name: :class:`str`
        
        :param stickers: List of stickers to be added to the set; must be non-empty. All stickers must have the same format. For TGS stickers, uploadStickerFile must be used before the sticker is shown
        :type stickers: :class:`list[InputSticker]`
        
        :param source: Source of the sticker set; may be empty if unknown
        :type source: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSet`
        """
        _constructor = CreateNewStickerSet.construct if skip_validation else CreateNewStickerSet

        return await self.client.request(
            _constructor(
                user_id=user_id,
                title=title,
                name=name,
                stickers=stickers,
                source=source,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_new_supergroup_chat(
            self,
            title: str,
            is_channel: bool,
            param_description: typing.Optional[str],
            location: ChatLocation,
            for_import: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Creates a new supergroup or channel and sends a corresponding messageSupergroupChatCreate. Returns the newly created chat
        
        :param title: Title of the new chat; 1-128 characters
        :type title: :class:`str`
        
        :param is_channel: Pass true to create a channel chat
        :type is_channel: :class:`bool`
        
        :param param_description: Chat description; 0-255 characters, defaults to None
        :type param_description: :class:`str`, optional
        
        :param location: Chat location if a location-based supergroup is being created; pass null to create an ordinary supergroup chat
        :type location: :class:`ChatLocation`
        
        :param for_import: Pass true to create a supergroup for importing messages using importMessage
        :type for_import: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """
        _constructor = CreateNewSupergroupChat.construct if skip_validation else CreateNewSupergroupChat

        return await self.client.request(
            _constructor(
                title=title,
                is_channel=is_channel,
                param_description=param_description,
                location=location,
                for_import=for_import,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_private_chat(
            self,
            user_id: int,
            force: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Returns an existing chat corresponding to a given user
        
        :param user_id: User identifier
        :type user_id: :class:`int`
        
        :param force: Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect
        :type force: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """
        _constructor = CreatePrivateChat.construct if skip_validation else CreatePrivateChat

        return await self.client.request(
            _constructor(
                user_id=user_id,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_secret_chat(
            self,
            secret_chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Returns an existing chat corresponding to a known secret chat
        
        :param secret_chat_id: Secret chat identifier
        :type secret_chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """
        _constructor = CreateSecretChat.construct if skip_validation else CreateSecretChat

        return await self.client.request(
            _constructor(
                secret_chat_id=secret_chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_supergroup_chat(
            self,
            supergroup_id: int,
            force: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Returns an existing chat corresponding to a known supergroup or channel
        
        :param supergroup_id: Supergroup or channel identifier
        :type supergroup_id: :class:`int`
        
        :param force: Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect
        :type force: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """
        _constructor = CreateSupergroupChat.construct if skip_validation else CreateSupergroupChat

        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_temporary_password(
            self,
            password: str,
            valid_for: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TemporaryPasswordState:
        """
        Creates a new temporary password for processing payments
        
        :param password: Persistent user password
        :type password: :class:`str`
        
        :param valid_for: Time during which the temporary password will be valid, in seconds; must be between 60 and 86400
        :type valid_for: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TemporaryPasswordState`
        """
        _constructor = CreateTemporaryPassword.construct if skip_validation else CreateTemporaryPassword

        return await self.client.request(
            _constructor(
                password=password,
                valid_for=valid_for,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_video_chat(
            self,
            chat_id: int,
            title: str,
            start_date: int,
            is_rtmp_stream: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> GroupCallId:
        """
        Creates a video chat (a group call bound to a chat). Available only for basic groups, supergroups and channels; requires can_manage_video_chats rights
        
        :param chat_id: Identifier of a chat in which the video chat will be created
        :type chat_id: :class:`int`
        
        :param title: Group call title; if empty, chat title will be used
        :type title: :class:`str`
        
        :param start_date: Point in time (Unix timestamp) when the group call is supposed to be started by an administrator; 0 to start the video chat immediately. The date must be at least 10 seconds and at most 8 days in the future
        :type start_date: :class:`int`
        
        :param is_rtmp_stream: Pass true to create an RTMP stream instead of an ordinary video chat; requires creator privileges
        :type is_rtmp_stream: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.GroupCallId`
        """
        _constructor = CreateVideoChat.construct if skip_validation else CreateVideoChat

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                title=title,
                start_date=start_date,
                is_rtmp_stream=is_rtmp_stream,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_account(
            self,
            reason: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes the account of the current user, deleting all information associated with the user from the server. The phone number of the account can be used to create a new account. Can be called before authorization when the current authorization state is authorizationStateWaitPassword
        
        :param reason: The reason why the account was deleted; optional
        :type reason: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteAccount.construct if skip_validation else DeleteAccount

        return await self.client.request(
            _constructor(
                reason=reason,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_all_call_messages(
            self,
            revoke: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes all call messages
        
        :param revoke: Pass true to delete the messages for all users
        :type revoke: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteAllCallMessages.construct if skip_validation else DeleteAllCallMessages

        return await self.client.request(
            _constructor(
                revoke=revoke,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_all_revoked_chat_invite_links(
            self,
            chat_id: int,
            creator_user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes all revoked chat invite links created by a given chat administrator. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param creator_user_id: User identifier of a chat administrator, which links will be deleted. Must be an identifier of the current user for non-owner
        :type creator_user_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteAllRevokedChatInviteLinks.construct if skip_validation else DeleteAllRevokedChatInviteLinks

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                creator_user_id=creator_user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes a chat along with all messages in the corresponding chat for all chat members. For group chats this will release the username and remove all members. Use the field chat.can_be_deleted_for_all_users to find whether the method can be applied to the chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteChat.construct if skip_validation else DeleteChat

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_chat_filter(
            self,
            chat_filter_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes existing chat filter
        
        :param chat_filter_id: Chat filter identifier
        :type chat_filter_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteChatFilter.construct if skip_validation else DeleteChatFilter

        return await self.client.request(
            _constructor(
                chat_filter_id=chat_filter_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_chat_history(
            self,
            chat_id: int,
            remove_from_chat_list: bool,
            revoke: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes all messages in the chat. Use chat.can_be_deleted_only_for_self and chat.can_be_deleted_for_all_users fields to find whether and how the method can be applied to the chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param remove_from_chat_list: Pass true to remove the chat from all chat lists
        :type remove_from_chat_list: :class:`bool`
        
        :param revoke: Pass true to delete chat history for all users
        :type revoke: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteChatHistory.construct if skip_validation else DeleteChatHistory

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                remove_from_chat_list=remove_from_chat_list,
                revoke=revoke,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_chat_messages_by_date(
            self,
            chat_id: int,
            min_date: int,
            max_date: int,
            revoke: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes all messages between the specified dates in a chat. Supported only for private chats and basic groups. Messages sent in the last 30 seconds will not be deleted
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param min_date: The minimum date of the messages to delete
        :type min_date: :class:`int`
        
        :param max_date: The maximum date of the messages to delete
        :type max_date: :class:`int`
        
        :param revoke: Pass true to delete chat messages for all users; private chats only
        :type revoke: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteChatMessagesByDate.construct if skip_validation else DeleteChatMessagesByDate

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                min_date=min_date,
                max_date=max_date,
                revoke=revoke,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_chat_messages_by_sender(
            self,
            chat_id: int,
            sender_id: MessageSender,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes all messages sent by the specified message sender in a chat. Supported only for supergroups; requires can_delete_messages administrator privileges
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param sender_id: Identifier of the sender of messages to delete
        :type sender_id: :class:`MessageSender`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteChatMessagesBySender.construct if skip_validation else DeleteChatMessagesBySender

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                sender_id=sender_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_chat_reply_markup(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes the default reply markup from a chat. Must be called after a one-time keyboard or a ForceReply reply markup has been used. UpdateChatReplyMarkup will be sent if the reply markup is changed
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param message_id: The message identifier of the used keyboard
        :type message_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteChatReplyMarkup.construct if skip_validation else DeleteChatReplyMarkup

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_commands(
            self,
            scope: BotCommandScope,
            language_code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes commands supported by the bot for the given user scope and language; for bots only
        
        :param scope: The scope to which the commands are relevant; pass null to delete commands in the default bot command scope
        :type scope: :class:`BotCommandScope`
        
        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :type language_code: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteCommands.construct if skip_validation else DeleteCommands

        return await self.client.request(
            _constructor(
                scope=scope,
                language_code=language_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_file(
            self,
            file_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes a file from the TDLib file cache
        
        :param file_id: Identifier of the file to delete
        :type file_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteFile.construct if skip_validation else DeleteFile

        return await self.client.request(
            _constructor(
                file_id=file_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_language_pack(
            self,
            language_pack_id: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes all information about a language pack in the current localization target. The language pack which is currently in use (including base language pack) or is being synchronized can't be deleted. Can be called before authorization
        
        :param language_pack_id: Identifier of the language pack to delete
        :type language_pack_id: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteLanguagePack.construct if skip_validation else DeleteLanguagePack

        return await self.client.request(
            _constructor(
                language_pack_id=language_pack_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_messages(
            self,
            chat_id: int,
            message_ids: list[int],
            revoke: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes messages
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param message_ids: Identifiers of the messages to be deleted
        :type message_ids: :class:`list[int]`
        
        :param revoke: Pass true to delete messages for all chat members. Always true for supergroups, channels and secret chats
        :type revoke: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteMessages.construct if skip_validation else DeleteMessages

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=revoke,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_passport_element(
            self,
            type_: PassportElementType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes a Telegram Passport element
        
        :param type_: Element type
        :type type_: :class:`PassportElementType`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeletePassportElement.construct if skip_validation else DeletePassportElement

        return await self.client.request(
            _constructor(
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_profile_photo(
            self,
            profile_photo_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes a profile photo
        
        :param profile_photo_id: Identifier of the profile photo to delete
        :type profile_photo_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteProfilePhoto.construct if skip_validation else DeleteProfilePhoto

        return await self.client.request(
            _constructor(
                profile_photo_id=profile_photo_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_revoked_chat_invite_link(
            self,
            chat_id: int,
            invite_link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes revoked chat invite links. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param invite_link: Invite link to revoke
        :type invite_link: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DeleteRevokedChatInviteLink.construct if skip_validation else DeleteRevokedChatInviteLink

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_saved_credentials(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Deletes saved credentials for all payment provider bots
        
        """
        return await self.client.request(
            DeleteSavedCredentials(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_saved_order_info(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Deletes saved order information
        
        """
        return await self.client.request(
            DeleteSavedOrderInfo(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def destroy(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Closes the TDLib instance, destroying all local data without a proper logout. The current user session will remain in the list of all active sessions. All local data will be destroyed. After the destruction completes updateAuthorizationState with authorizationStateClosed will be sent. Can be called before authorization
        
        """
        return await self.client.request(
            Destroy(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def disable_proxy(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Disables the currently enabled proxy. Can be called before authorization
        
        """
        return await self.client.request(
            DisableProxy(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def discard_call(
            self,
            call_id: int,
            is_disconnected: bool,
            duration: int,
            is_video: bool,
            connection_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Discards a call
        
        :param call_id: Call identifier
        :type call_id: :class:`int`
        
        :param is_disconnected: Pass true if the user was disconnected
        :type is_disconnected: :class:`bool`
        
        :param duration: The call duration, in seconds
        :type duration: :class:`int`
        
        :param is_video: Pass true if the call was a video call
        :type is_video: :class:`bool`
        
        :param connection_id: Identifier of the connection used during the call
        :type connection_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DiscardCall.construct if skip_validation else DiscardCall

        return await self.client.request(
            _constructor(
                call_id=call_id,
                is_disconnected=is_disconnected,
                duration=duration,
                is_video=is_video,
                connection_id=connection_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def disconnect_all_websites(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Disconnects all websites from the current user's Telegram account
        
        """
        return await self.client.request(
            DisconnectAllWebsites(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def disconnect_website(
            self,
            website_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Disconnects website from the current user's Telegram account
        
        :param website_id: Website identifier
        :type website_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = DisconnectWebsite.construct if skip_validation else DisconnectWebsite

        return await self.client.request(
            _constructor(
                website_id=website_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def download_file(
            self,
            file_id: int,
            priority: int,
            offset: int,
            limit: int,
            synchronous: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> File:
        """
        Downloads a file from the cloud. Download progress and completion of the download will be notified through updateFile updates
        
        :param file_id: Identifier of the file to download
        :type file_id: :class:`int`
        
        :param priority: Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first
        :type priority: :class:`int`
        
        :param offset: The starting position from which the file needs to be downloaded
        :type offset: :class:`int`
        
        :param limit: Number of bytes which need to be downloaded starting from the "offset" position before the download will automatically be canceled; use 0 to download without a limit
        :type limit: :class:`int`
        
        :param synchronous: Pass true to return response only after the file download has succeeded, has failed, has been canceled, or a new downloadFile request with different offset/limit parameters was sent; pass false to return file state immediately, just after the download has been started
        :type synchronous: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.File`
        """
        _constructor = DownloadFile.construct if skip_validation else DownloadFile

        return await self.client.request(
            _constructor(
                file_id=file_id,
                priority=priority,
                offset=offset,
                limit=limit,
                synchronous=synchronous,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_chat_filter(
            self,
            chat_filter_id: int,
            filter_: ChatFilter,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatFilterInfo:
        """
        Edits existing chat filter. Returns information about the edited chat filter
        
        :param chat_filter_id: Chat filter identifier
        :type chat_filter_id: :class:`int`
        
        :param filter_: The edited chat filter
        :type filter_: :class:`ChatFilter`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatFilterInfo`
        """
        _constructor = EditChatFilter.construct if skip_validation else EditChatFilter

        return await self.client.request(
            _constructor(
                chat_filter_id=chat_filter_id,
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_chat_invite_link(
            self,
            chat_id: int,
            invite_link: str,
            name: typing.Optional[str],
            expiration_date: int,
            member_limit: int,
            creates_join_request: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLink:
        """
        Edits a non-primary invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param invite_link: Invite link to be edited
        :type invite_link: :class:`str`
        
        :param name: Invite link name; 0-32 characters, defaults to None
        :type name: :class:`str`, optional
        
        :param expiration_date: Point in time (Unix timestamp) when the link will expire; pass 0 if never
        :type expiration_date: :class:`int`
        
        :param member_limit: The maximum number of chat members that can join the chat via the link simultaneously; 0-99999; pass 0 if not limited
        :type member_limit: :class:`int`
        
        :param creates_join_request: Pass true if users joining the chat via the link need to be approved by chat administrators. In this case, member_limit must be 0
        :type creates_join_request: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLink`
        """
        _constructor = EditChatInviteLink.construct if skip_validation else EditChatInviteLink

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                invite_link=invite_link,
                name=name,
                expiration_date=expiration_date,
                member_limit=member_limit,
                creates_join_request=creates_join_request,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_custom_language_pack_info(
            self,
            info: LanguagePackInfo,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Edits information about a custom local language pack in the current localization target. Can be called before authorization
        
        :param info: New information about the custom local language pack
        :type info: :class:`LanguagePackInfo`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = EditCustomLanguagePackInfo.construct if skip_validation else EditCustomLanguagePackInfo

        return await self.client.request(
            _constructor(
                info=info,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_inline_message_caption(
            self,
            inline_message_id: str,
            reply_markup: ReplyMarkup,
            caption: FormattedText,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Edits the caption of an inline message sent via a bot; for bots only
        
        :param inline_message_id: Inline message identifier
        :type inline_message_id: :class:`str`
        
        :param reply_markup: The new message reply markup; pass null if none
        :type reply_markup: :class:`ReplyMarkup`
        
        :param caption: New message content caption; pass null to remove caption; 0-GetOption("message_caption_length_max") characters
        :type caption: :class:`FormattedText`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = EditInlineMessageCaption.construct if skip_validation else EditInlineMessageCaption

        return await self.client.request(
            _constructor(
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
                caption=caption,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_inline_message_live_location(
            self,
            inline_message_id: str,
            reply_markup: ReplyMarkup,
            location: Location,
            heading: int,
            proximity_alert_radius: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Edits the content of a live location in an inline message sent via a bot; for bots only
        
        :param inline_message_id: Inline message identifier
        :type inline_message_id: :class:`str`
        
        :param reply_markup: The new message reply markup; pass null if none
        :type reply_markup: :class:`ReplyMarkup`
        
        :param location: New location content of the message; pass null to stop sharing the live location
        :type location: :class:`Location`
        
        :param heading: The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
        :type heading: :class:`int`
        
        :param proximity_alert_radius: The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled
        :type proximity_alert_radius: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = EditInlineMessageLiveLocation.construct if skip_validation else EditInlineMessageLiveLocation

        return await self.client.request(
            _constructor(
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
                location=location,
                heading=heading,
                proximity_alert_radius=proximity_alert_radius,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_inline_message_media(
            self,
            inline_message_id: str,
            reply_markup: ReplyMarkup,
            input_message_content: InputMessageContent,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Edits the content of a message with an animation, an audio, a document, a photo or a video in an inline message sent via a bot; for bots only
        
        :param inline_message_id: Inline message identifier
        :type inline_message_id: :class:`str`
        
        :param reply_markup: The new message reply markup; pass null if none; for bots only
        :type reply_markup: :class:`ReplyMarkup`
        
        :param input_message_content: New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo
        :type input_message_content: :class:`InputMessageContent`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = EditInlineMessageMedia.construct if skip_validation else EditInlineMessageMedia

        return await self.client.request(
            _constructor(
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
                input_message_content=input_message_content,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_inline_message_reply_markup(
            self,
            inline_message_id: str,
            reply_markup: ReplyMarkup,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Edits the reply markup of an inline message sent via a bot; for bots only
        
        :param inline_message_id: Inline message identifier
        :type inline_message_id: :class:`str`
        
        :param reply_markup: The new message reply markup; pass null if none
        :type reply_markup: :class:`ReplyMarkup`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = EditInlineMessageReplyMarkup.construct if skip_validation else EditInlineMessageReplyMarkup

        return await self.client.request(
            _constructor(
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_inline_message_text(
            self,
            inline_message_id: str,
            reply_markup: ReplyMarkup,
            input_message_content: InputMessageContent,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Edits the text of an inline text or game message sent via a bot; for bots only
        
        :param inline_message_id: Inline message identifier
        :type inline_message_id: :class:`str`
        
        :param reply_markup: The new message reply markup; pass null if none
        :type reply_markup: :class:`ReplyMarkup`
        
        :param input_message_content: New text content of the message. Must be of type inputMessageText
        :type input_message_content: :class:`InputMessageContent`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = EditInlineMessageText.construct if skip_validation else EditInlineMessageText

        return await self.client.request(
            _constructor(
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
                input_message_content=input_message_content,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_message_caption(
            self,
            chat_id: int,
            message_id: int,
            reply_markup: ReplyMarkup,
            caption: FormattedText,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Edits the message content caption. Returns the edited message after the edit is completed on the server side
        
        :param chat_id: The chat the message belongs to
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param reply_markup: The new message reply markup; pass null if none; for bots only
        :type reply_markup: :class:`ReplyMarkup`
        
        :param caption: New message content caption; 0-GetOption("message_caption_length_max") characters; pass null to remove caption
        :type caption: :class:`FormattedText`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = EditMessageCaption.construct if skip_validation else EditMessageCaption

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
                caption=caption,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_message_live_location(
            self,
            chat_id: int,
            message_id: int,
            reply_markup: ReplyMarkup,
            location: Location,
            heading: int,
            proximity_alert_radius: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Edits the message content of a live location. Messages can be edited for a limited period of time specified in the live location. Returns the edited message after the edit is completed on the server side
        
        :param chat_id: The chat the message belongs to
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param reply_markup: The new message reply markup; pass null if none; for bots only
        :type reply_markup: :class:`ReplyMarkup`
        
        :param location: New location content of the message; pass null to stop sharing the live location
        :type location: :class:`Location`
        
        :param heading: The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
        :type heading: :class:`int`
        
        :param proximity_alert_radius: The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled
        :type proximity_alert_radius: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = EditMessageLiveLocation.construct if skip_validation else EditMessageLiveLocation

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
                location=location,
                heading=heading,
                proximity_alert_radius=proximity_alert_radius,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_message_media(
            self,
            chat_id: int,
            message_id: int,
            reply_markup: ReplyMarkup,
            input_message_content: InputMessageContent,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Edits the content of a message with an animation, an audio, a document, a photo or a video, including message caption. If only the caption needs to be edited, use editMessageCaption instead. The media can't be edited if the message was set to self-destruct or to a self-destructing media. The type of message content in an album can't be changed with exception of replacing a photo with a video or vice versa. Returns the edited message after the edit is completed on the server side
        
        :param chat_id: The chat the message belongs to
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param reply_markup: The new message reply markup; pass null if none; for bots only
        :type reply_markup: :class:`ReplyMarkup`
        
        :param input_message_content: New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo
        :type input_message_content: :class:`InputMessageContent`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = EditMessageMedia.construct if skip_validation else EditMessageMedia

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
                input_message_content=input_message_content,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_message_reply_markup(
            self,
            chat_id: int,
            message_id: int,
            reply_markup: ReplyMarkup,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Edits the message reply markup; for bots only. Returns the edited message after the edit is completed on the server side
        
        :param chat_id: The chat the message belongs to
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param reply_markup: The new message reply markup; pass null if none
        :type reply_markup: :class:`ReplyMarkup`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = EditMessageReplyMarkup.construct if skip_validation else EditMessageReplyMarkup

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_message_scheduling_state(
            self,
            chat_id: int,
            message_id: int,
            scheduling_state: MessageSchedulingState,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Edits the time when a scheduled message will be sent. Scheduling state of all messages in the same album or forwarded together with the message will be also changed
        
        :param chat_id: The chat the message belongs to
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param scheduling_state: The new message scheduling state; pass null to send the message immediately
        :type scheduling_state: :class:`MessageSchedulingState`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = EditMessageSchedulingState.construct if skip_validation else EditMessageSchedulingState

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                scheduling_state=scheduling_state,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_message_text(
            self,
            chat_id: int,
            message_id: int,
            reply_markup: ReplyMarkup,
            input_message_content: InputMessageContent,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Edits the text of a message (or a text of a game message). Returns the edited message after the edit is completed on the server side
        
        :param chat_id: The chat the message belongs to
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param reply_markup: The new message reply markup; pass null if none; for bots only
        :type reply_markup: :class:`ReplyMarkup`
        
        :param input_message_content: New text content of the message. Must be of type inputMessageText
        :type input_message_content: :class:`InputMessageContent`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = EditMessageText.construct if skip_validation else EditMessageText

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
                input_message_content=input_message_content,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_proxy(
            self,
            proxy_id: int,
            server: str,
            port: int,
            enable: bool,
            type_: ProxyType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Proxy:
        """
        Edits an existing proxy server for network requests. Can be called before authorization
        
        :param proxy_id: Proxy identifier
        :type proxy_id: :class:`int`
        
        :param server: Proxy server IP address
        :type server: :class:`str`
        
        :param port: Proxy server port
        :type port: :class:`int`
        
        :param enable: Pass true to immediately enable the proxy
        :type enable: :class:`bool`
        
        :param type_: Proxy type
        :type type_: :class:`ProxyType`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Proxy`
        """
        _constructor = EditProxy.construct if skip_validation else EditProxy

        return await self.client.request(
            _constructor(
                proxy_id=proxy_id,
                server=server,
                port=port,
                enable=enable,
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def enable_proxy(
            self,
            proxy_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Enables a proxy. Only one proxy can be enabled at a time. Can be called before authorization
        
        :param proxy_id: Proxy identifier
        :type proxy_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = EnableProxy.construct if skip_validation else EnableProxy

        return await self.client.request(
            _constructor(
                proxy_id=proxy_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def end_group_call(
            self,
            group_call_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Ends a group call. Requires groupCall.can_be_managed
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = EndGroupCall.construct if skip_validation else EndGroupCall

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def end_group_call_recording(
            self,
            group_call_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Ends recording of an active group call. Requires groupCall.can_be_managed group call flag
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = EndGroupCallRecording.construct if skip_validation else EndGroupCallRecording

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def end_group_call_screen_sharing(
            self,
            group_call_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Ends screen sharing in a joined group call
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = EndGroupCallScreenSharing.construct if skip_validation else EndGroupCallScreenSharing

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def finish_file_generation(
            self,
            generation_id: int,
            error: Error,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Finishes the file generation
        
        :param generation_id: The identifier of the generation process
        :type generation_id: :class:`int`
        
        :param error: If passed, the file generation has failed and must be terminated; pass null if the file generation succeeded
        :type error: :class:`Error`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = FinishFileGeneration.construct if skip_validation else FinishFileGeneration

        return await self.client.request(
            _constructor(
                generation_id=generation_id,
                error=error,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def forward_messages(
            self,
            chat_id: int,
            from_chat_id: int,
            message_ids: list[int],
            options: MessageSendOptions,
            send_copy: bool,
            remove_caption: bool,
            only_preview: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Forwards previously sent messages. Returns the forwarded messages in the same order as the message identifiers passed in message_ids. If a message can't be forwarded, null will be returned instead of the message
        
        :param chat_id: Identifier of the chat to which to forward messages
        :type chat_id: :class:`int`
        
        :param from_chat_id: Identifier of the chat from which to forward messages
        :type from_chat_id: :class:`int`
        
        :param message_ids: Identifiers of the messages to forward. Message identifiers must be in a strictly increasing order. At most 100 messages can be forwarded simultaneously
        :type message_ids: :class:`list[int]`
        
        :param options: Options to be used to send the messages; pass null to use default options
        :type options: :class:`MessageSendOptions`
        
        :param send_copy: Pass true to copy content of the messages without reference to the original sender. Always true if the messages are forwarded to a secret chat or are local
        :type send_copy: :class:`bool`
        
        :param remove_caption: Pass true to remove media captions of message copies. Ignored if send_copy is false
        :type remove_caption: :class:`bool`
        
        :param only_preview: Pass true to get fake messages instead of actually forwarding them
        :type only_preview: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """
        _constructor = ForwardMessages.construct if skip_validation else ForwardMessages

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                from_chat_id=from_chat_id,
                message_ids=message_ids,
                options=options,
                send_copy=send_copy,
                remove_caption=remove_caption,
                only_preview=only_preview,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_account_ttl(self, *, request_id: str = None, request_timeout: int = None) -> AccountTtl:
        """
        Returns the period of inactivity after which the account of the current user will automatically be deleted
        
        """
        return await self.client.request(
            GetAccountTtl(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_active_live_location_messages(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> Messages:
        """
        Returns all active live locations that need to be updated by the application. The list is persistent across application restarts only if the message database is used
        
        """
        return await self.client.request(
            GetActiveLiveLocationMessages(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_active_sessions(self, *, request_id: str = None, request_timeout: int = None) -> Sessions:
        """
        Returns all active sessions of the current user
        
        """
        return await self.client.request(
            GetActiveSessions(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_all_passport_elements(
            self,
            password: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PassportElements:
        """
        Returns all available Telegram Passport elements
        
        :param password: Password of the current user
        :type password: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PassportElements`
        """
        _constructor = GetAllPassportElements.construct if skip_validation else GetAllPassportElements

        return await self.client.request(
            _constructor(
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_animated_emoji(
            self,
            emoji: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> AnimatedEmoji:
        """
        Returns an animated emoji corresponding to a given emoji. Returns a 404 error if the emoji has no animated emoji
        
        :param emoji: The emoji
        :type emoji: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AnimatedEmoji`
        """
        _constructor = GetAnimatedEmoji.construct if skip_validation else GetAnimatedEmoji

        return await self.client.request(
            _constructor(
                emoji=emoji,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_application_config(self, *, request_id: str = None, request_timeout: int = None) -> JsonValue:
        """
        Returns application config, provided by the server. Can be called before authorization
        
        """
        return await self.client.request(
            GetApplicationConfig(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_application_download_link(self, *, request_id: str = None, request_timeout: int = None) -> HttpUrl:
        """
        Returns the link for downloading official Telegram application to be used when the current user invites friends to Telegram
        
        """
        return await self.client.request(
            GetApplicationDownloadLink(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_archived_sticker_sets(
            self,
            is_masks: bool,
            offset_sticker_set_id: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSets:
        """
        Returns a list of archived sticker sets
        
        :param is_masks: Pass true to return mask stickers sets; pass false to return ordinary sticker sets
        :type is_masks: :class:`bool`
        
        :param offset_sticker_set_id: Identifier of the sticker set from which to return the result
        :type offset_sticker_set_id: :class:`int`
        
        :param limit: The maximum number of sticker sets to return; up to 100
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSets`
        """
        _constructor = GetArchivedStickerSets.construct if skip_validation else GetArchivedStickerSets

        return await self.client.request(
            _constructor(
                is_masks=is_masks,
                offset_sticker_set_id=offset_sticker_set_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_attached_sticker_sets(
            self,
            file_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSets:
        """
        Returns a list of sticker sets attached to a file. Currently, only photos and videos can have attached sticker sets
        
        :param file_id: File identifier
        :type file_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSets`
        """
        _constructor = GetAttachedStickerSets.construct if skip_validation else GetAttachedStickerSets

        return await self.client.request(
            _constructor(
                file_id=file_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_attachment_menu_bot(
            self,
            bot_user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> AttachmentMenuBot:
        """
        Returns information about a bot that can be added to attachment menu
        
        :param bot_user_id: Bot's user identifier
        :type bot_user_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AttachmentMenuBot`
        """
        _constructor = GetAttachmentMenuBot.construct if skip_validation else GetAttachmentMenuBot

        return await self.client.request(
            _constructor(
                bot_user_id=bot_user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_authorization_state(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> AuthorizationState:
        """
        Returns the current authorization state; this is an offline request. For informational purposes only. Use updateAuthorizationState instead to maintain the current authorization state. Can be called before initialization
        
        """
        return await self.client.request(
            GetAuthorizationState(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_auto_download_settings_presets(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> AutoDownloadSettingsPresets:
        """
        Returns auto-download settings presets for the current user
        
        """
        return await self.client.request(
            GetAutoDownloadSettingsPresets(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_background_url(
            self,
            name: str,
            type_: BackgroundType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> HttpUrl:
        """
        Constructs a persistent HTTP URL for a background
        
        :param name: Background name
        :type name: :class:`str`
        
        :param type_: Background type
        :type type_: :class:`BackgroundType`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """
        _constructor = GetBackgroundUrl.construct if skip_validation else GetBackgroundUrl

        return await self.client.request(
            _constructor(
                name=name,
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_backgrounds(
            self,
            for_dark_theme: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Backgrounds:
        """
        Returns backgrounds installed by the user
        
        :param for_dark_theme: Pass true to order returned backgrounds for a dark theme
        :type for_dark_theme: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Backgrounds`
        """
        _constructor = GetBackgrounds.construct if skip_validation else GetBackgrounds

        return await self.client.request(
            _constructor(
                for_dark_theme=for_dark_theme,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_bank_card_info(
            self,
            bank_card_number: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> BankCardInfo:
        """
        Returns information about a bank card
        
        :param bank_card_number: The bank card number
        :type bank_card_number: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.BankCardInfo`
        """
        _constructor = GetBankCardInfo.construct if skip_validation else GetBankCardInfo

        return await self.client.request(
            _constructor(
                bank_card_number=bank_card_number,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_basic_group(
            self,
            basic_group_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> BasicGroup:
        """
        Returns information about a basic group by its identifier. This is an offline request if the current user is not a bot
        
        :param basic_group_id: Basic group identifier
        :type basic_group_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.BasicGroup`
        """
        _constructor = GetBasicGroup.construct if skip_validation else GetBasicGroup

        return await self.client.request(
            _constructor(
                basic_group_id=basic_group_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_basic_group_full_info(
            self,
            basic_group_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> BasicGroupFullInfo:
        """
        Returns full information about a basic group by its identifier
        
        :param basic_group_id: Basic group identifier
        :type basic_group_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.BasicGroupFullInfo`
        """
        _constructor = GetBasicGroupFullInfo.construct if skip_validation else GetBasicGroupFullInfo

        return await self.client.request(
            _constructor(
                basic_group_id=basic_group_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_blocked_message_senders(
            self,
            offset: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageSenders:
        """
        Returns users and chats that were blocked by the current user
        
        :param offset: Number of users and chats to skip in the result; must be non-negative
        :type offset: :class:`int`
        
        :param limit: The maximum number of users and chats to return; up to 100
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageSenders`
        """
        _constructor = GetBlockedMessageSenders.construct if skip_validation else GetBlockedMessageSenders

        return await self.client.request(
            _constructor(
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_callback_query_answer(
            self,
            chat_id: int,
            message_id: int,
            payload: CallbackQueryPayload,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> CallbackQueryAnswer:
        """
        Sends a callback query to a bot and returns an answer. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires
        
        :param chat_id: Identifier of the chat with the message
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message from which the query originated
        :type message_id: :class:`int`
        
        :param payload: Query payload
        :type payload: :class:`CallbackQueryPayload`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.CallbackQueryAnswer`
        """
        _constructor = GetCallbackQueryAnswer.construct if skip_validation else GetCallbackQueryAnswer

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                payload=payload,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_callback_query_message(
            self,
            chat_id: int,
            message_id: int,
            callback_query_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Returns information about a message with the callback button that originated a callback query; for bots only
        
        :param chat_id: Identifier of the chat the message belongs to
        :type chat_id: :class:`int`
        
        :param message_id: Message identifier
        :type message_id: :class:`int`
        
        :param callback_query_id: Identifier of the callback query
        :type callback_query_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = GetCallbackQueryMessage.construct if skip_validation else GetCallbackQueryMessage

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                callback_query_id=callback_query_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Returns information about a chat by its identifier, this is an offline request if the current user is not a bot
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """
        _constructor = GetChat.construct if skip_validation else GetChat

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_administrators(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatAdministrators:
        """
        Returns a list of administrators of the chat with their custom titles
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatAdministrators`
        """
        _constructor = GetChatAdministrators.construct if skip_validation else GetChatAdministrators

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_available_message_senders(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageSenders:
        """
        Returns list of message sender identifiers, which can be used to send messages in a chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageSenders`
        """
        _constructor = GetChatAvailableMessageSenders.construct if skip_validation else GetChatAvailableMessageSenders

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_event_log(
            self,
            chat_id: int,
            query: str,
            from_event_id: int,
            limit: int,
            filters: ChatEventLogFilters,
            user_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatEvents:
        """
        Returns a list of service actions taken by chat members and administrators in the last 48 hours. Available only for supergroups and channels. Requires administrator rights. Returns results in reverse chronological order (i. e., in order of decreasing event_id)
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param query: Search query by which to filter events
        :type query: :class:`str`
        
        :param from_event_id: Identifier of an event from which to return results. Use 0 to get results from the latest events
        :type from_event_id: :class:`int`
        
        :param limit: The maximum number of events to return; up to 100
        :type limit: :class:`int`
        
        :param filters: The types of events to return; pass null to get chat events of all types
        :type filters: :class:`ChatEventLogFilters`
        
        :param user_ids: User identifiers by which to filter events. By default, events relating to all users will be returned
        :type user_ids: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatEvents`
        """
        _constructor = GetChatEventLog.construct if skip_validation else GetChatEventLog

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                query=query,
                from_event_id=from_event_id,
                limit=limit,
                filters=filters,
                user_ids=user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_filter(
            self,
            chat_filter_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatFilter:
        """
        Returns information about a chat filter by its identifier
        
        :param chat_filter_id: Chat filter identifier
        :type chat_filter_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatFilter`
        """
        _constructor = GetChatFilter.construct if skip_validation else GetChatFilter

        return await self.client.request(
            _constructor(
                chat_filter_id=chat_filter_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_filter_default_icon_name(
            self,
            filter_: ChatFilter,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Returns default icon name for a filter. Can be called synchronously
        
        :param filter_: Chat filter
        :type filter_: :class:`ChatFilter`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """
        _constructor = GetChatFilterDefaultIconName.construct if skip_validation else GetChatFilterDefaultIconName

        return await self.client.request(
            _constructor(
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_history(
            self,
            chat_id: int,
            from_message_id: int,
            offset: int,
            limit: int,
            only_local: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Returns messages in a chat. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib. This is an offline request if only_local is true
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param from_message_id: Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        :type from_message_id: :class:`int`
        
        :param offset: Specify 0 to get results from exactly the from_message_id or a negative offset up to 99 to get additionally some newer messages
        :type offset: :class:`int`
        
        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`int`
        
        :param only_local: Pass true to get only messages that are available without sending network requests
        :type only_local: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """
        _constructor = GetChatHistory.construct if skip_validation else GetChatHistory

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                from_message_id=from_message_id,
                offset=offset,
                limit=limit,
                only_local=only_local,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_invite_link(
            self,
            chat_id: int,
            invite_link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLink:
        """
        Returns information about an invite link. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param invite_link: Invite link to get
        :type invite_link: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLink`
        """
        _constructor = GetChatInviteLink.construct if skip_validation else GetChatInviteLink

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_invite_link_counts(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLinkCounts:
        """
        Returns list of chat administrators with number of their invite links. Requires owner privileges in the chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLinkCounts`
        """
        _constructor = GetChatInviteLinkCounts.construct if skip_validation else GetChatInviteLinkCounts

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_invite_link_members(
            self,
            chat_id: int,
            invite_link: str,
            offset_member: ChatInviteLinkMember,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLinkMembers:
        """
        Returns chat members joined a chat via an invite link. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param invite_link: Invite link for which to return chat members
        :type invite_link: :class:`str`
        
        :param offset_member: A chat member from which to return next chat members; pass null to get results from the beginning
        :type offset_member: :class:`ChatInviteLinkMember`
        
        :param limit: The maximum number of chat members to return; up to 100
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLinkMembers`
        """
        _constructor = GetChatInviteLinkMembers.construct if skip_validation else GetChatInviteLinkMembers

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                invite_link=invite_link,
                offset_member=offset_member,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_invite_links(
            self,
            chat_id: int,
            creator_user_id: int,
            is_revoked: bool,
            offset_date: int,
            offset_invite_link: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLinks:
        """
        Returns invite links for a chat created by specified administrator. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param creator_user_id: User identifier of a chat administrator. Must be an identifier of the current user for non-owner
        :type creator_user_id: :class:`int`
        
        :param is_revoked: Pass true if revoked links needs to be returned instead of active or expired
        :type is_revoked: :class:`bool`
        
        :param offset_date: Creation date of an invite link starting after which to return invite links; use 0 to get results from the beginning
        :type offset_date: :class:`int`
        
        :param offset_invite_link: Invite link starting after which to return invite links; use empty string to get results from the beginning
        :type offset_invite_link: :class:`str`
        
        :param limit: The maximum number of invite links to return; up to 100
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLinks`
        """
        _constructor = GetChatInviteLinks.construct if skip_validation else GetChatInviteLinks

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                creator_user_id=creator_user_id,
                is_revoked=is_revoked,
                offset_date=offset_date,
                offset_invite_link=offset_invite_link,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_join_requests(
            self,
            chat_id: int,
            invite_link: str,
            query: str,
            offset_request: ChatJoinRequest,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatJoinRequests:
        """
        Returns pending join requests in a chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param invite_link: Invite link for which to return join requests. If empty, all join requests will be returned. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        :type invite_link: :class:`str`
        
        :param query: A query to search for in the first names, last names and usernames of the users to return
        :type query: :class:`str`
        
        :param offset_request: A chat join request from which to return next requests; pass null to get results from the beginning
        :type offset_request: :class:`ChatJoinRequest`
        
        :param limit: The maximum number of requests to join the chat to return
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatJoinRequests`
        """
        _constructor = GetChatJoinRequests.construct if skip_validation else GetChatJoinRequests

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                invite_link=invite_link,
                query=query,
                offset_request=offset_request,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_lists_to_add_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatLists:
        """
        Returns chat lists to which the chat can be added. This is an offline request
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatLists`
        """
        _constructor = GetChatListsToAddChat.construct if skip_validation else GetChatListsToAddChat

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_member(
            self,
            chat_id: int,
            member_id: MessageSender,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatMember:
        """
        Returns information about a single member of a chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param member_id: Member identifier
        :type member_id: :class:`MessageSender`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatMember`
        """
        _constructor = GetChatMember.construct if skip_validation else GetChatMember

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                member_id=member_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_message_by_date(
            self,
            chat_id: int,
            date: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Returns the last message sent in a chat no later than the specified date
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param date: Point in time (Unix timestamp) relative to which to search for messages
        :type date: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = GetChatMessageByDate.construct if skip_validation else GetChatMessageByDate

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                date=date,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_message_calendar(
            self,
            chat_id: int,
            filter_: SearchMessagesFilter,
            from_message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageCalendar:
        """
        Returns information about the next messages of the specified type in the chat split by days. Returns the results in reverse chronological order. Can return partial result for the last returned day. Behavior of this method depends on the value of the option "utc_time_offset"
        
        :param chat_id: Identifier of the chat in which to return information about messages
        :type chat_id: :class:`int`
        
        :param filter_: Filter for message content. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function
        :type filter_: :class:`SearchMessagesFilter`
        
        :param from_message_id: The message identifier from which to return information about messages; use 0 to get results from the last message
        :type from_message_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageCalendar`
        """
        _constructor = GetChatMessageCalendar.construct if skip_validation else GetChatMessageCalendar

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                filter=filter_,
                from_message_id=from_message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_message_count(
            self,
            chat_id: int,
            filter_: SearchMessagesFilter,
            return_local: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Count:
        """
        Returns approximate number of messages of the specified type in the chat
        
        :param chat_id: Identifier of the chat in which to count messages
        :type chat_id: :class:`int`
        
        :param filter_: Filter for message content; searchMessagesFilterEmpty is unsupported in this function
        :type filter_: :class:`SearchMessagesFilter`
        
        :param return_local: Pass true to get the number of messages without sending network requests, or -1 if the number of messages is unknown locally
        :type return_local: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Count`
        """
        _constructor = GetChatMessageCount.construct if skip_validation else GetChatMessageCount

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                filter=filter_,
                return_local=return_local,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_notification_settings_exceptions(
            self,
            scope: NotificationSettingsScope,
            compare_sound: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Returns list of chats with non-default notification settings
        
        :param scope: If specified, only chats from the scope will be returned; pass null to return chats from all scopes
        :type scope: :class:`NotificationSettingsScope`
        
        :param compare_sound: Pass true to include in the response chats with only non-default sound
        :type compare_sound: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """
        _constructor = GetChatNotificationSettingsExceptions.construct if skip_validation else GetChatNotificationSettingsExceptions

        return await self.client.request(
            _constructor(
                scope=scope,
                compare_sound=compare_sound,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_pinned_message(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Returns information about a newest pinned message in the chat
        
        :param chat_id: Identifier of the chat the message belongs to
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = GetChatPinnedMessage.construct if skip_validation else GetChatPinnedMessage

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_scheduled_messages(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Returns all scheduled messages in a chat. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id)
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """
        _constructor = GetChatScheduledMessages.construct if skip_validation else GetChatScheduledMessages

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_sparse_message_positions(
            self,
            chat_id: int,
            filter_: SearchMessagesFilter,
            from_message_id: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessagePositions:
        """
        Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation. Returns the results in reverse chronological order (i.e., in order of decreasing message_id). Cannot be used in secret chats or with searchMessagesFilterFailedToSend filter without an enabled message database
        
        :param chat_id: Identifier of the chat in which to return information about message positions
        :type chat_id: :class:`int`
        
        :param filter_: Filter for message content. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function
        :type filter_: :class:`SearchMessagesFilter`
        
        :param from_message_id: The message identifier from which to return information about message positions
        :type from_message_id: :class:`int`
        
        :param limit: The expected number of message positions to be returned; 50-2000. A smaller number of positions can be returned, if there are not enough appropriate messages
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessagePositions`
        """
        _constructor = GetChatSparseMessagePositions.construct if skip_validation else GetChatSparseMessagePositions

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                filter=filter_,
                from_message_id=from_message_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_sponsored_message(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> SponsoredMessage:
        """
        Returns sponsored message to be shown in a chat; for channel chats only. Returns a 404 error if there is no sponsored message in the chat
        
        :param chat_id: Identifier of the chat
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.SponsoredMessage`
        """
        _constructor = GetChatSponsoredMessage.construct if skip_validation else GetChatSponsoredMessage

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_statistics(
            self,
            chat_id: int,
            is_dark: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatStatistics:
        """
        Returns detailed statistics about a chat. Currently, this method can be used only for supergroups and channels. Can be used only if supergroupFullInfo.can_get_statistics == true
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param is_dark: Pass true if a dark theme is used by the application
        :type is_dark: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatStatistics`
        """
        _constructor = GetChatStatistics.construct if skip_validation else GetChatStatistics

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                is_dark=is_dark,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chats(
            self,
            chat_list: ChatList,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Returns an ordered list of chats from the beginning of a chat list. For informational purposes only. Use loadChats and updates processing instead to maintain chat lists in a consistent state
        
        :param chat_list: The chat list in which to return chats; pass null to get chats from the main chat list
        :type chat_list: :class:`ChatList`
        
        :param limit: The maximum number of chats to be returned
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """
        _constructor = GetChats.construct if skip_validation else GetChats

        return await self.client.request(
            _constructor(
                chat_list=chat_list,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_commands(
            self,
            scope: BotCommandScope,
            language_code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> BotCommands:
        """
        Returns the list of commands supported by the bot for the given user scope and language; for bots only
        
        :param scope: The scope to which the commands are relevant; pass null to get commands in the default bot command scope
        :type scope: :class:`BotCommandScope`
        
        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :type language_code: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.BotCommands`
        """
        _constructor = GetCommands.construct if skip_validation else GetCommands

        return await self.client.request(
            _constructor(
                scope=scope,
                language_code=language_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_connected_websites(self, *, request_id: str = None, request_timeout: int = None) -> ConnectedWebsites:
        """
        Returns all website where the current user used Telegram to log in
        
        """
        return await self.client.request(
            GetConnectedWebsites(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_contacts(self, *, request_id: str = None, request_timeout: int = None) -> Users:
        """
        Returns all user contacts
        
        """
        return await self.client.request(
            GetContacts(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_countries(self, *, request_id: str = None, request_timeout: int = None) -> Countries:
        """
        Returns information about existing countries. Can be called before authorization
        
        """
        return await self.client.request(
            GetCountries(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_country_code(self, *, request_id: str = None, request_timeout: int = None) -> Text:
        """
        Uses the current IP address to find the current country. Returns two-letter ISO 3166-1 alpha-2 country code. Can be called before authorization
        
        """
        return await self.client.request(
            GetCountryCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_created_public_chats(
            self,
            type_: PublicChatType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Returns a list of public chats of the specified type, owned by the user
        
        :param type_: Type of the public chats to return
        :type type_: :class:`PublicChatType`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """
        _constructor = GetCreatedPublicChats.construct if skip_validation else GetCreatedPublicChats

        return await self.client.request(
            _constructor(
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_current_state(self, *, request_id: str = None, request_timeout: int = None) -> Updates:
        """
        Returns all updates needed to restore current TDLib state, i.e. all actual UpdateAuthorizationState/UpdateUser/UpdateNewChat and others. This is especially useful if TDLib is run in a separate process. Can be called before initialization
        
        """
        return await self.client.request(
            GetCurrentState(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_database_statistics(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> DatabaseStatistics:
        """
        Returns database statistics
        
        """
        return await self.client.request(
            GetDatabaseStatistics(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_deep_link_info(
            self,
            link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> DeepLinkInfo:
        """
        Returns information about a tg:// deep link. Use "tg://need_update_for_some_feature" or "tg:some_unsupported_feature" for testing. Returns a 404 error for unknown links. Can be called before authorization
        
        :param link: The link
        :type link: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.DeepLinkInfo`
        """
        _constructor = GetDeepLinkInfo.construct if skip_validation else GetDeepLinkInfo

        return await self.client.request(
            _constructor(
                link=link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_emoji_suggestions_url(
            self,
            language_code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> HttpUrl:
        """
        Returns an HTTP URL which can be used to automatically log in to the translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation
        
        :param language_code: Language code for which the emoji replacements will be suggested
        :type language_code: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """
        _constructor = GetEmojiSuggestionsUrl.construct if skip_validation else GetEmojiSuggestionsUrl

        return await self.client.request(
            _constructor(
                language_code=language_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_external_link(
            self,
            link: str,
            allow_write_access: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> HttpUrl:
        """
        Returns an HTTP URL which can be used to automatically authorize the current user on a website after clicking an HTTP link. Use the method getExternalLinkInfo to find whether a prior user confirmation is needed
        
        :param link: The HTTP link
        :type link: :class:`str`
        
        :param allow_write_access: Pass true if the current user allowed the bot, returned in getExternalLinkInfo, to send them messages
        :type allow_write_access: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """
        _constructor = GetExternalLink.construct if skip_validation else GetExternalLink

        return await self.client.request(
            _constructor(
                link=link,
                allow_write_access=allow_write_access,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_external_link_info(
            self,
            link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> LoginUrlInfo:
        """
        Returns information about an action to be done when the current user clicks an external link. Don't use this method for links from secret chats if web page preview is disabled in secret chats
        
        :param link: The link
        :type link: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.LoginUrlInfo`
        """
        _constructor = GetExternalLinkInfo.construct if skip_validation else GetExternalLinkInfo

        return await self.client.request(
            _constructor(
                link=link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_favorite_stickers(self, *, request_id: str = None, request_timeout: int = None) -> Stickers:
        """
        Returns favorite stickers
        
        """
        return await self.client.request(
            GetFavoriteStickers(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_file(
            self,
            file_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> File:
        """
        Returns information about a file; this is an offline request
        
        :param file_id: Identifier of the file to get
        :type file_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.File`
        """
        _constructor = GetFile.construct if skip_validation else GetFile

        return await self.client.request(
            _constructor(
                file_id=file_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_file_downloaded_prefix_size(
            self,
            file_id: int,
            offset: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Count:
        """
        Returns file downloaded prefix size from a given offset, in bytes
        
        :param file_id: Identifier of the file
        :type file_id: :class:`int`
        
        :param offset: Offset from which downloaded prefix size needs to be calculated
        :type offset: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Count`
        """
        _constructor = GetFileDownloadedPrefixSize.construct if skip_validation else GetFileDownloadedPrefixSize

        return await self.client.request(
            _constructor(
                file_id=file_id,
                offset=offset,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_file_extension(
            self,
            mime_type: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Returns the extension of a file, guessed by its MIME type. Returns an empty string on failure. Can be called synchronously
        
        :param mime_type: The MIME type of the file
        :type mime_type: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """
        _constructor = GetFileExtension.construct if skip_validation else GetFileExtension

        return await self.client.request(
            _constructor(
                mime_type=mime_type,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_file_mime_type(
            self,
            file_name: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Returns the MIME type of a file, guessed by its extension. Returns an empty string on failure. Can be called synchronously
        
        :param file_name: The name of the file or path to the file
        :type file_name: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """
        _constructor = GetFileMimeType.construct if skip_validation else GetFileMimeType

        return await self.client.request(
            _constructor(
                file_name=file_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_game_high_scores(
            self,
            chat_id: int,
            message_id: int,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> GameHighScores:
        """
        Returns the high scores for a game and some part of the high score table in the range of the specified user; for bots only
        
        :param chat_id: The chat that contains the message with the game
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param user_id: User identifier
        :type user_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.GameHighScores`
        """
        _constructor = GetGameHighScores.construct if skip_validation else GetGameHighScores

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_group_call(
            self,
            group_call_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> GroupCall:
        """
        Returns information about a group call
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.GroupCall`
        """
        _constructor = GetGroupCall.construct if skip_validation else GetGroupCall

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_group_call_invite_link(
            self,
            group_call_id: int,
            can_self_unmute: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> HttpUrl:
        """
        Returns invite link to a video chat in a public chat
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param can_self_unmute: Pass true if the invite link needs to contain an invite hash, passing which to joinGroupCall would allow the invited user to unmute themselves. Requires groupCall.can_be_managed group call flag
        :type can_self_unmute: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """
        _constructor = GetGroupCallInviteLink.construct if skip_validation else GetGroupCallInviteLink

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                can_self_unmute=can_self_unmute,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_group_call_stream_segment(
            self,
            group_call_id: int,
            time_offset: int,
            scale: int,
            channel_id: int,
            video_quality: GroupCallVideoQuality,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FilePart:
        """
        Returns a file with a segment of a group call stream in a modified OGG format for audio or MPEG-4 format for video
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param time_offset: Point in time when the stream segment begins; Unix timestamp in milliseconds
        :type time_offset: :class:`int`
        
        :param scale: Segment duration scale; 0-1. Segment's duration is 1000/(2**scale) milliseconds
        :type scale: :class:`int`
        
        :param channel_id: Identifier of an audio/video channel to get as received from tgcalls
        :type channel_id: :class:`int`
        
        :param video_quality: Video quality as received from tgcalls; pass null to get the worst available quality
        :type video_quality: :class:`GroupCallVideoQuality`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FilePart`
        """
        _constructor = GetGroupCallStreamSegment.construct if skip_validation else GetGroupCallStreamSegment

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                time_offset=time_offset,
                scale=scale,
                channel_id=channel_id,
                video_quality=video_quality,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_group_call_streams(
            self,
            group_call_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> GroupCallStreams:
        """
        Returns information about available group call streams
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.GroupCallStreams`
        """
        _constructor = GetGroupCallStreams.construct if skip_validation else GetGroupCallStreams

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_groups_in_common(
            self,
            user_id: int,
            offset_chat_id: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Returns a list of common group chats with a given user. Chats are sorted by their type and creation date
        
        :param user_id: User identifier
        :type user_id: :class:`int`
        
        :param offset_chat_id: Chat identifier starting from which to return chats; use 0 for the first request
        :type offset_chat_id: :class:`int`
        
        :param limit: The maximum number of chats to be returned; up to 100
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """
        _constructor = GetGroupsInCommon.construct if skip_validation else GetGroupsInCommon

        return await self.client.request(
            _constructor(
                user_id=user_id,
                offset_chat_id=offset_chat_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_imported_contact_count(self, *, request_id: str = None, request_timeout: int = None) -> Count:
        """
        Returns the total number of imported contacts
        
        """
        return await self.client.request(
            GetImportedContactCount(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_inactive_supergroup_chats(self, *, request_id: str = None, request_timeout: int = None) -> Chats:
        """
        Returns a list of recently inactive supergroups and channels. Can be used when user reaches limit on the number of joined supergroups and channels and receives CHANNELS_TOO_MUCH error
        
        """
        return await self.client.request(
            GetInactiveSupergroupChats(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_inline_game_high_scores(
            self,
            inline_message_id: str,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> GameHighScores:
        """
        Returns game high scores and some part of the high score table in the range of the specified user; for bots only
        
        :param inline_message_id: Inline message identifier
        :type inline_message_id: :class:`str`
        
        :param user_id: User identifier
        :type user_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.GameHighScores`
        """
        _constructor = GetInlineGameHighScores.construct if skip_validation else GetInlineGameHighScores

        return await self.client.request(
            _constructor(
                inline_message_id=inline_message_id,
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_inline_query_results(
            self,
            bot_user_id: int,
            chat_id: int,
            user_location: Location,
            query: str,
            offset: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> InlineQueryResults:
        """
        Sends an inline query to a bot and returns its results. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires
        
        :param bot_user_id: The identifier of the target bot
        :type bot_user_id: :class:`int`
        
        :param chat_id: Identifier of the chat where the query was sent
        :type chat_id: :class:`int`
        
        :param user_location: Location of the user; pass null if unknown or the bot doesn't need user's location
        :type user_location: :class:`Location`
        
        :param query: Text of the query
        :type query: :class:`str`
        
        :param offset: Offset of the first entry to return
        :type offset: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.InlineQueryResults`
        """
        _constructor = GetInlineQueryResults.construct if skip_validation else GetInlineQueryResults

        return await self.client.request(
            _constructor(
                bot_user_id=bot_user_id,
                chat_id=chat_id,
                user_location=user_location,
                query=query,
                offset=offset,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_installed_sticker_sets(
            self,
            is_masks: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSets:
        """
        Returns a list of installed sticker sets
        
        :param is_masks: Pass true to return mask sticker sets; pass false to return ordinary sticker sets
        :type is_masks: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSets`
        """
        _constructor = GetInstalledStickerSets.construct if skip_validation else GetInstalledStickerSets

        return await self.client.request(
            _constructor(
                is_masks=is_masks,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_internal_link_type(
            self,
            link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> InternalLinkType:
        """
        Returns information about the type of an internal link. Returns a 404 error if the link is not internal. Can be called before authorization
        
        :param link: The link
        :type link: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.InternalLinkType`
        """
        _constructor = GetInternalLinkType.construct if skip_validation else GetInternalLinkType

        return await self.client.request(
            _constructor(
                link=link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_json_string(
            self,
            json_value: JsonValue,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Converts a JsonValue object to corresponding JSON-serialized string. Can be called synchronously
        
        :param json_value: The JsonValue object
        :type json_value: :class:`JsonValue`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """
        _constructor = GetJsonString.construct if skip_validation else GetJsonString

        return await self.client.request(
            _constructor(
                json_value=json_value,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_json_value(
            self,
            json_: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> JsonValue:
        """
        Converts a JSON-serialized string to corresponding JsonValue object. Can be called synchronously
        
        :param json_: The JSON-serialized string
        :type json_: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.JsonValue`
        """
        _constructor = GetJsonValue.construct if skip_validation else GetJsonValue

        return await self.client.request(
            _constructor(
                json=json_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_language_pack_info(
            self,
            language_pack_id: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> LanguagePackInfo:
        """
        Returns information about a language pack. Returned language pack identifier may be different from a provided one. Can be called before authorization
        
        :param language_pack_id: Language pack identifier
        :type language_pack_id: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.LanguagePackInfo`
        """
        _constructor = GetLanguagePackInfo.construct if skip_validation else GetLanguagePackInfo

        return await self.client.request(
            _constructor(
                language_pack_id=language_pack_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_language_pack_string(
            self,
            language_pack_database_path: str,
            localization_target: str,
            language_pack_id: str,
            key: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> LanguagePackStringValue:
        """
        Returns a string stored in the local database from the specified localization target and language pack by its key. Returns a 404 error if the string is not found. Can be called synchronously
        
        :param language_pack_database_path: Path to the language pack database in which strings are stored
        :type language_pack_database_path: :class:`str`
        
        :param localization_target: Localization target to which the language pack belongs
        :type localization_target: :class:`str`
        
        :param language_pack_id: Language pack identifier
        :type language_pack_id: :class:`str`
        
        :param key: Language pack key of the string to be returned
        :type key: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.LanguagePackStringValue`
        """
        _constructor = GetLanguagePackString.construct if skip_validation else GetLanguagePackString

        return await self.client.request(
            _constructor(
                language_pack_database_path=language_pack_database_path,
                localization_target=localization_target,
                language_pack_id=language_pack_id,
                key=key,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_language_pack_strings(
            self,
            language_pack_id: str,
            keys: list[str],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> LanguagePackStrings:
        """
        Returns strings from a language pack in the current localization target by their keys. Can be called before authorization
        
        :param language_pack_id: Language pack identifier of the strings to be returned
        :type language_pack_id: :class:`str`
        
        :param keys: Language pack keys of the strings to be returned; leave empty to request all available strings
        :type keys: :class:`list[str]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.LanguagePackStrings`
        """
        _constructor = GetLanguagePackStrings.construct if skip_validation else GetLanguagePackStrings

        return await self.client.request(
            _constructor(
                language_pack_id=language_pack_id,
                keys=keys,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_localization_target_info(
            self,
            only_local: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> LocalizationTargetInfo:
        """
        Returns information about the current localization target. This is an offline request if only_local is true. Can be called before authorization
        
        :param only_local: Pass true to get only locally available information without sending network requests
        :type only_local: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.LocalizationTargetInfo`
        """
        _constructor = GetLocalizationTargetInfo.construct if skip_validation else GetLocalizationTargetInfo

        return await self.client.request(
            _constructor(
                only_local=only_local,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_log_stream(self, *, request_id: str = None, request_timeout: int = None) -> LogStream:
        """
        Returns information about currently used log stream for internal logging of TDLib. Can be called synchronously
        
        """
        return await self.client.request(
            GetLogStream(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_log_tag_verbosity_level(
            self,
            tag: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> LogVerbosityLevel:
        """
        Returns current verbosity level for a specified TDLib internal log tag. Can be called synchronously
        
        :param tag: Logging tag to change verbosity level
        :type tag: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.LogVerbosityLevel`
        """
        _constructor = GetLogTagVerbosityLevel.construct if skip_validation else GetLogTagVerbosityLevel

        return await self.client.request(
            _constructor(
                tag=tag,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_log_tags(self, *, request_id: str = None, request_timeout: int = None) -> LogTags:
        """
        Returns list of available TDLib internal log tags, for example, ["actor", "binlog", "connections", "notifications", "proxy"]. Can be called synchronously
        
        """
        return await self.client.request(
            GetLogTags(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_log_verbosity_level(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> LogVerbosityLevel:
        """
        Returns current verbosity level of the internal logging of TDLib. Can be called synchronously
        
        """
        return await self.client.request(
            GetLogVerbosityLevel(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_login_url(
            self,
            chat_id: int,
            message_id: int,
            button_id: int,
            allow_write_access: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> HttpUrl:
        """
        Returns an HTTP URL which can be used to automatically authorize the user on a website after clicking an inline button of type inlineKeyboardButtonTypeLoginUrl. Use the method getLoginUrlInfo to find whether a prior user confirmation is needed. If an error is returned, then the button must be handled as an ordinary URL button
        
        :param chat_id: Chat identifier of the message with the button
        :type chat_id: :class:`int`
        
        :param message_id: Message identifier of the message with the button
        :type message_id: :class:`int`
        
        :param button_id: Button identifier
        :type button_id: :class:`int`
        
        :param allow_write_access: Pass true to allow the bot to send messages to the current user
        :type allow_write_access: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """
        _constructor = GetLoginUrl.construct if skip_validation else GetLoginUrl

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                button_id=button_id,
                allow_write_access=allow_write_access,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_login_url_info(
            self,
            chat_id: int,
            message_id: int,
            button_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> LoginUrlInfo:
        """
        Returns information about a button of type inlineKeyboardButtonTypeLoginUrl. The method needs to be called when the user presses the button
        
        :param chat_id: Chat identifier of the message with the button
        :type chat_id: :class:`int`
        
        :param message_id: Message identifier of the message with the button
        :type message_id: :class:`int`
        
        :param button_id: Button identifier
        :type button_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.LoginUrlInfo`
        """
        _constructor = GetLoginUrlInfo.construct if skip_validation else GetLoginUrlInfo

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                button_id=button_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_map_thumbnail_file(
            self,
            location: Location,
            zoom: int,
            width: int,
            height: int,
            scale: int,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> File:
        """
        Returns information about a file with a map thumbnail in PNG format. Only map thumbnail files with size less than 1MB can be downloaded
        
        :param location: Location of the map center
        :type location: :class:`Location`
        
        :param zoom: Map zoom level; 13-20
        :type zoom: :class:`int`
        
        :param width: Map width in pixels before applying scale; 16-1024
        :type width: :class:`int`
        
        :param height: Map height in pixels before applying scale; 16-1024
        :type height: :class:`int`
        
        :param scale: Map scale; 1-3
        :type scale: :class:`int`
        
        :param chat_id: Identifier of a chat in which the thumbnail will be shown. Use 0 if unknown
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.File`
        """
        _constructor = GetMapThumbnailFile.construct if skip_validation else GetMapThumbnailFile

        return await self.client.request(
            _constructor(
                location=location,
                zoom=zoom,
                width=width,
                height=height,
                scale=scale,
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_markdown_text(
            self,
            text: FormattedText,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FormattedText:
        """
        Replaces text entities with Markdown formatting in a human-friendly format. Entities that can't be represented in Markdown unambiguously are kept as is. Can be called synchronously
        
        :param text: The text
        :type text: :class:`FormattedText`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FormattedText`
        """
        _constructor = GetMarkdownText.construct if skip_validation else GetMarkdownText

        return await self.client.request(
            _constructor(
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_me(self, *, request_id: str = None, request_timeout: int = None) -> User:
        """
        Returns the current user
        
        """
        return await self.client.request(
            GetMe(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_menu_button(
            self,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> BotMenuButton:
        """
        Returns menu button set by the bot for the given user; for bots only
        
        :param user_id: Identifier of the user or 0 to get the default menu button
        :type user_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.BotMenuButton`
        """
        _constructor = GetMenuButton.construct if skip_validation else GetMenuButton

        return await self.client.request(
            _constructor(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Returns information about a message
        
        :param chat_id: Identifier of the chat the message belongs to
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message to get
        :type message_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = GetMessage.construct if skip_validation else GetMessage

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_added_reactions(
            self,
            chat_id: int,
            message_id: int,
            reaction: str,
            offset: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> AddedReactions:
        """
        Returns reactions added for a message, along with their sender
        
        :param chat_id: Identifier of the chat to which the message belongs
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param reaction: If non-empty, only added reactions with the specified text representation will be returned
        :type reaction: :class:`str`
        
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :type offset: :class:`str`
        
        :param limit: The maximum number of reactions to be returned; must be positive and can't be greater than 100
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AddedReactions`
        """
        _constructor = GetMessageAddedReactions.construct if skip_validation else GetMessageAddedReactions

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                reaction=reaction,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_available_reactions(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> AvailableReactions:
        """
        Returns reactions, which can be added to a message. The list can change after updateReactions, updateChatAvailableReactions for the chat, or updateMessageInteractionInfo for the message
        
        :param chat_id: Identifier of the chat to which the message belongs
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AvailableReactions`
        """
        _constructor = GetMessageAvailableReactions.construct if skip_validation else GetMessageAvailableReactions

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_embedding_code(
            self,
            chat_id: int,
            message_id: int,
            for_album: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Returns an HTML code for embedding the message. Available only for messages in supergroups and channels with a username
        
        :param chat_id: Identifier of the chat to which the message belongs
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param for_album: Pass true to return an HTML code for embedding of the whole media album
        :type for_album: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """
        _constructor = GetMessageEmbeddingCode.construct if skip_validation else GetMessageEmbeddingCode

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                for_album=for_album,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_file_type(
            self,
            message_file_head: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageFileType:
        """
        Returns information about a file with messages exported from another app
        
        :param message_file_head: Beginning of the message file; up to 100 first lines
        :type message_file_head: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageFileType`
        """
        _constructor = GetMessageFileType.construct if skip_validation else GetMessageFileType

        return await self.client.request(
            _constructor(
                message_file_head=message_file_head,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_import_confirmation_text(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Returns a confirmation text to be shown to the user before starting message import
        
        :param chat_id: Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info administrator right
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """
        _constructor = GetMessageImportConfirmationText.construct if skip_validation else GetMessageImportConfirmationText

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_link(
            self,
            chat_id: int,
            message_id: int,
            media_timestamp: int,
            for_album: bool,
            for_comment: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageLink:
        """
        Returns an HTTPS link to a message in a chat. Available only for already sent messages in supergroups and channels, or if message.can_get_media_timestamp_links and a media timestamp link is generated. This is an offline request
        
        :param chat_id: Identifier of the chat to which the message belongs
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param media_timestamp: If not 0, timestamp from which the video/audio/video note/voice note playing must start, in seconds. The media can be in the message content or in its web page preview
        :type media_timestamp: :class:`int`
        
        :param for_album: Pass true to create a link for the whole media album
        :type for_album: :class:`bool`
        
        :param for_comment: Pass true to create a link to the message as a channel post comment, or from a message thread
        :type for_comment: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageLink`
        """
        _constructor = GetMessageLink.construct if skip_validation else GetMessageLink

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                media_timestamp=media_timestamp,
                for_album=for_album,
                for_comment=for_comment,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_link_info(
            self,
            url: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageLinkInfo:
        """
        Returns information about a public or private message link. Can be called for any internal link of the type internalLinkTypeMessage
        
        :param url: The message link
        :type url: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageLinkInfo`
        """
        _constructor = GetMessageLinkInfo.construct if skip_validation else GetMessageLinkInfo

        return await self.client.request(
            _constructor(
                url=url,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_locally(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Returns information about a message, if it is available without sending network request. This is an offline request
        
        :param chat_id: Identifier of the chat the message belongs to
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message to get
        :type message_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = GetMessageLocally.construct if skip_validation else GetMessageLocally

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_public_forwards(
            self,
            chat_id: int,
            message_id: int,
            offset: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FoundMessages:
        """
        Returns forwarded copies of a channel message to different public channels. For optimal performance, the number of returned messages is chosen by TDLib
        
        :param chat_id: Chat identifier of the message
        :type chat_id: :class:`int`
        
        :param message_id: Message identifier
        :type message_id: :class:`int`
        
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :type offset: :class:`str`
        
        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FoundMessages`
        """
        _constructor = GetMessagePublicForwards.construct if skip_validation else GetMessagePublicForwards

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_statistics(
            self,
            chat_id: int,
            message_id: int,
            is_dark: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageStatistics:
        """
        Returns detailed statistics about a message. Can be used only if message.can_get_statistics == true
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param message_id: Message identifier
        :type message_id: :class:`int`
        
        :param is_dark: Pass true if a dark theme is used by the application
        :type is_dark: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageStatistics`
        """
        _constructor = GetMessageStatistics.construct if skip_validation else GetMessageStatistics

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                is_dark=is_dark,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_thread(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageThreadInfo:
        """
        Returns information about a message thread. Can be used only if message.can_get_message_thread == true
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageThreadInfo`
        """
        _constructor = GetMessageThread.construct if skip_validation else GetMessageThread

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_thread_history(
            self,
            chat_id: int,
            message_id: int,
            from_message_id: int,
            offset: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Returns messages in a message thread of a message. Can be used only if message.can_get_message_thread == true. Message thread of a channel message is in the channel's linked supergroup. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param message_id: Message identifier, which thread history needs to be returned
        :type message_id: :class:`int`
        
        :param from_message_id: Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        :type from_message_id: :class:`int`
        
        :param offset: Specify 0 to get results from exactly the from_message_id or a negative offset up to 99 to get additionally some newer messages
        :type offset: :class:`int`
        
        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """
        _constructor = GetMessageThreadHistory.construct if skip_validation else GetMessageThreadHistory

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                from_message_id=from_message_id,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_viewers(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Users:
        """
        Returns viewers of a recent outgoing message in a basic group or a supergroup chat. For video notes and voice notes only users, opened content of the message, are returned. The method can be called if message.can_get_viewers == true
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Users`
        """
        _constructor = GetMessageViewers.construct if skip_validation else GetMessageViewers

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_messages(
            self,
            chat_id: int,
            message_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Returns information about messages. If a message is not found, returns null on the corresponding position of the result
        
        :param chat_id: Identifier of the chat the messages belong to
        :type chat_id: :class:`int`
        
        :param message_ids: Identifiers of the messages to get
        :type message_ids: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """
        _constructor = GetMessages.construct if skip_validation else GetMessages

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_ids=message_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_network_statistics(
            self,
            only_current: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> NetworkStatistics:
        """
        Returns network data usage statistics. Can be called before authorization
        
        :param only_current: Pass true to get statistics only for the current library launch
        :type only_current: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.NetworkStatistics`
        """
        _constructor = GetNetworkStatistics.construct if skip_validation else GetNetworkStatistics

        return await self.client.request(
            _constructor(
                only_current=only_current,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_option(
            self,
            name: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> OptionValue:
        """
        Returns the value of an option by its name. (Check the list of available options on https://core.telegram.org/tdlib/options.) Can be called before authorization
        
        :param name: The name of the option
        :type name: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.OptionValue`
        """
        _constructor = GetOption.construct if skip_validation else GetOption

        return await self.client.request(
            _constructor(
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_passport_authorization_form(
            self,
            bot_user_id: int,
            scope: str,
            public_key: str,
            nonce: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PassportAuthorizationForm:
        """
        Returns a Telegram Passport authorization form for sharing data with a service
        
        :param bot_user_id: User identifier of the service's bot
        :type bot_user_id: :class:`int`
        
        :param scope: Telegram Passport element types requested by the service
        :type scope: :class:`str`
        
        :param public_key: Service's public key
        :type public_key: :class:`str`
        
        :param nonce: Unique request identifier provided by the service
        :type nonce: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PassportAuthorizationForm`
        """
        _constructor = GetPassportAuthorizationForm.construct if skip_validation else GetPassportAuthorizationForm

        return await self.client.request(
            _constructor(
                bot_user_id=bot_user_id,
                scope=scope,
                public_key=public_key,
                nonce=nonce,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_passport_authorization_form_available_elements(
            self,
            autorization_form_id: int,
            password: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PassportElementsWithErrors:
        """
        Returns already available Telegram Passport elements suitable for completing a Telegram Passport authorization form. Result can be received only once for each authorization form
        
        :param autorization_form_id: Authorization form identifier
        :type autorization_form_id: :class:`int`
        
        :param password: Password of the current user
        :type password: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PassportElementsWithErrors`
        """
        _constructor = GetPassportAuthorizationFormAvailableElements.construct if skip_validation else GetPassportAuthorizationFormAvailableElements

        return await self.client.request(
            _constructor(
                autorization_form_id=autorization_form_id,
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_passport_element(
            self,
            type_: PassportElementType,
            password: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PassportElement:
        """
        Returns one of the available Telegram Passport elements
        
        :param type_: Telegram Passport element type
        :type type_: :class:`PassportElementType`
        
        :param password: Password of the current user
        :type password: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PassportElement`
        """
        _constructor = GetPassportElement.construct if skip_validation else GetPassportElement

        return await self.client.request(
            _constructor(
                type=type_,
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_password_state(self, *, request_id: str = None, request_timeout: int = None) -> PasswordState:
        """
        Returns the current state of 2-step verification
        
        """
        return await self.client.request(
            GetPasswordState(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_payment_form(
            self,
            chat_id: int,
            message_id: int,
            theme: ThemeParameters,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PaymentForm:
        """
        Returns an invoice payment form. This method must be called when the user presses inlineKeyboardButtonBuy
        
        :param chat_id: Chat identifier of the Invoice message
        :type chat_id: :class:`int`
        
        :param message_id: Message identifier
        :type message_id: :class:`int`
        
        :param theme: Preferred payment form theme; pass null to use the default theme
        :type theme: :class:`ThemeParameters`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PaymentForm`
        """
        _constructor = GetPaymentForm.construct if skip_validation else GetPaymentForm

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                theme=theme,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_payment_receipt(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PaymentReceipt:
        """
        Returns information about a successful payment
        
        :param chat_id: Chat identifier of the PaymentSuccessful message
        :type chat_id: :class:`int`
        
        :param message_id: Message identifier
        :type message_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PaymentReceipt`
        """
        _constructor = GetPaymentReceipt.construct if skip_validation else GetPaymentReceipt

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_phone_number_info(
            self,
            phone_number_prefix: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PhoneNumberInfo:
        """
        Returns information about a phone number by its prefix. Can be called before authorization
        
        :param phone_number_prefix: The phone number prefix
        :type phone_number_prefix: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PhoneNumberInfo`
        """
        _constructor = GetPhoneNumberInfo.construct if skip_validation else GetPhoneNumberInfo

        return await self.client.request(
            _constructor(
                phone_number_prefix=phone_number_prefix,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_phone_number_info_sync(
            self,
            language_code: str,
            phone_number_prefix: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PhoneNumberInfo:
        """
        Returns information about a phone number by its prefix synchronously. getCountries must be called at least once after changing localization to the specified language if properly localized country information is expected. Can be called synchronously
        
        :param language_code: A two-letter ISO 639-1 language code for country information localization
        :type language_code: :class:`str`
        
        :param phone_number_prefix: The phone number prefix
        :type phone_number_prefix: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PhoneNumberInfo`
        """
        _constructor = GetPhoneNumberInfoSync.construct if skip_validation else GetPhoneNumberInfoSync

        return await self.client.request(
            _constructor(
                language_code=language_code,
                phone_number_prefix=phone_number_prefix,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_poll_voters(
            self,
            chat_id: int,
            message_id: int,
            option_id: int,
            offset: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Users:
        """
        Returns users voted for the specified option in a non-anonymous polls. For optimal performance, the number of returned users is chosen by TDLib
        
        :param chat_id: Identifier of the chat to which the poll belongs
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message containing the poll
        :type message_id: :class:`int`
        
        :param option_id: 0-based identifier of the answer option
        :type option_id: :class:`int`
        
        :param offset: Number of users to skip in the result; must be non-negative
        :type offset: :class:`int`
        
        :param limit: The maximum number of users to be returned; must be positive and can't be greater than 50. For optimal performance, the number of returned users is chosen by TDLib and can be smaller than the specified limit, even if the end of the voter list has not been reached
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Users`
        """
        _constructor = GetPollVoters.construct if skip_validation else GetPollVoters

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                option_id=option_id,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_preferred_country_language(
            self,
            country_code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Returns an IETF language tag of the language preferred in the country, which must be used to fill native fields in Telegram Passport personal details. Returns a 404 error if unknown
        
        :param country_code: A two-letter ISO 3166-1 alpha-2 country code
        :type country_code: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """
        _constructor = GetPreferredCountryLanguage.construct if skip_validation else GetPreferredCountryLanguage

        return await self.client.request(
            _constructor(
                country_code=country_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_proxies(self, *, request_id: str = None, request_timeout: int = None) -> Proxies:
        """
        Returns list of proxies that are currently set up. Can be called before authorization
        
        """
        return await self.client.request(
            GetProxies(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_proxy_link(
            self,
            proxy_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> HttpUrl:
        """
        Returns an HTTPS link, which can be used to add a proxy. Available only for SOCKS5 and MTProto proxies. Can be called before authorization
        
        :param proxy_id: Proxy identifier
        :type proxy_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """
        _constructor = GetProxyLink.construct if skip_validation else GetProxyLink

        return await self.client.request(
            _constructor(
                proxy_id=proxy_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_push_receiver_id(
            self,
            payload: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PushReceiverId:
        """
        Returns a globally unique push notification subscription identifier for identification of an account, which has received a push notification. Can be called synchronously
        
        :param payload: JSON-encoded push notification payload
        :type payload: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PushReceiverId`
        """
        _constructor = GetPushReceiverId.construct if skip_validation else GetPushReceiverId

        return await self.client.request(
            _constructor(
                payload=payload,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_recent_inline_bots(self, *, request_id: str = None, request_timeout: int = None) -> Users:
        """
        Returns up to 20 recently used inline bots in the order of their last usage
        
        """
        return await self.client.request(
            GetRecentInlineBots(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_recent_stickers(
            self,
            is_attached: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Stickers:
        """
        Returns a list of recently used stickers
        
        :param is_attached: Pass true to return stickers and masks that were recently attached to photos or video files; pass false to return recently sent stickers
        :type is_attached: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Stickers`
        """
        _constructor = GetRecentStickers.construct if skip_validation else GetRecentStickers

        return await self.client.request(
            _constructor(
                is_attached=is_attached,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_recently_opened_chats(
            self,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Returns recently opened chats, this is an offline request. Returns chats in the order of last opening
        
        :param limit: The maximum number of chats to be returned
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """
        _constructor = GetRecentlyOpenedChats.construct if skip_validation else GetRecentlyOpenedChats

        return await self.client.request(
            _constructor(
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_recently_visited_t_me_urls(
            self,
            referrer: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TMeUrls:
        """
        Returns t.me URLs recently visited by a newly registered user
        
        :param referrer: Google Play referrer to identify the user
        :type referrer: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TMeUrls`
        """
        _constructor = GetRecentlyVisitedTMeUrls.construct if skip_validation else GetRecentlyVisitedTMeUrls

        return await self.client.request(
            _constructor(
                referrer=referrer,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_recommended_chat_filters(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> RecommendedChatFilters:
        """
        Returns recommended chat filters for the current user
        
        """
        return await self.client.request(
            GetRecommendedChatFilters(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_recovery_email_address(
            self,
            password: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> RecoveryEmailAddress:
        """
        Returns a 2-step verification recovery email address that was previously set up. This method can be used to verify a password provided by the user
        
        :param password: The password for the current user
        :type password: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.RecoveryEmailAddress`
        """
        _constructor = GetRecoveryEmailAddress.construct if skip_validation else GetRecoveryEmailAddress

        return await self.client.request(
            _constructor(
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_remote_file(
            self,
            remote_file_id: str,
            file_type: FileType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> File:
        """
        Returns information about a file by its remote ID; this is an offline request. Can be used to register a URL as a file for further uploading, or sending as a message. Even the request succeeds, the file can be used only if it is still accessible to the user. For example, if the file is from a message, then the message must be not deleted and accessible to the user. If the file database is disabled, then the corresponding object with the file must be preloaded by the application
        
        :param remote_file_id: Remote identifier of the file to get
        :type remote_file_id: :class:`str`
        
        :param file_type: File type; pass null if unknown
        :type file_type: :class:`FileType`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.File`
        """
        _constructor = GetRemoteFile.construct if skip_validation else GetRemoteFile

        return await self.client.request(
            _constructor(
                remote_file_id=remote_file_id,
                file_type=file_type,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_replied_message(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Returns information about a message that is replied by a given message. Also returns the pinned message, the game message, and the invoice message for messages of the types messagePinMessage, messageGameScore, and messagePaymentSuccessful respectively
        
        :param chat_id: Identifier of the chat the message belongs to
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the reply message
        :type message_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = GetRepliedMessage.construct if skip_validation else GetRepliedMessage

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_saved_animations(self, *, request_id: str = None, request_timeout: int = None) -> Animations:
        """
        Returns saved animations
        
        """
        return await self.client.request(
            GetSavedAnimations(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_saved_notification_sound(
            self,
            notification_sound_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> NotificationSounds:
        """
        Returns saved notification sound by its identifier. Returns a 404 error if there is no saved notification sound with the specified identifier
        
        :param notification_sound_id: Identifier of the notification sound
        :type notification_sound_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.NotificationSounds`
        """
        _constructor = GetSavedNotificationSound.construct if skip_validation else GetSavedNotificationSound

        return await self.client.request(
            _constructor(
                notification_sound_id=notification_sound_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_saved_notification_sounds(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> NotificationSounds:
        """
        Returns list of saved notification sounds. If a sound isn't in the list, then default sound needs to be used
        
        """
        return await self.client.request(
            GetSavedNotificationSounds(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_saved_order_info(self, *, request_id: str = None, request_timeout: int = None) -> OrderInfo:
        """
        Returns saved order information. Returns a 404 error if there is no saved order information
        
        """
        return await self.client.request(
            GetSavedOrderInfo(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_scope_notification_settings(
            self,
            scope: NotificationSettingsScope,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ScopeNotificationSettings:
        """
        Returns the notification settings for chats of a given type
        
        :param scope: Types of chats for which to return the notification settings information
        :type scope: :class:`NotificationSettingsScope`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ScopeNotificationSettings`
        """
        _constructor = GetScopeNotificationSettings.construct if skip_validation else GetScopeNotificationSettings

        return await self.client.request(
            _constructor(
                scope=scope,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_secret_chat(
            self,
            secret_chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> SecretChat:
        """
        Returns information about a secret chat by its identifier. This is an offline request
        
        :param secret_chat_id: Secret chat identifier
        :type secret_chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.SecretChat`
        """
        _constructor = GetSecretChat.construct if skip_validation else GetSecretChat

        return await self.client.request(
            _constructor(
                secret_chat_id=secret_chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_statistical_graph(
            self,
            chat_id: int,
            token: str,
            x: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StatisticalGraph:
        """
        Loads an asynchronous or a zoomed in statistical graph
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param token: The token for graph loading
        :type token: :class:`str`
        
        :param x: X-value for zoomed in graph or 0 otherwise
        :type x: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StatisticalGraph`
        """
        _constructor = GetStatisticalGraph.construct if skip_validation else GetStatisticalGraph

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                token=token,
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_sticker_emojis(
            self,
            sticker: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Emojis:
        """
        Returns emoji corresponding to a sticker. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object
        
        :param sticker: Sticker file identifier
        :type sticker: :class:`InputFile`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Emojis`
        """
        _constructor = GetStickerEmojis.construct if skip_validation else GetStickerEmojis

        return await self.client.request(
            _constructor(
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_sticker_set(
            self,
            set_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSet:
        """
        Returns information about a sticker set by its identifier
        
        :param set_id: Identifier of the sticker set
        :type set_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSet`
        """
        _constructor = GetStickerSet.construct if skip_validation else GetStickerSet

        return await self.client.request(
            _constructor(
                set_id=set_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_stickers(
            self,
            emoji: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Stickers:
        """
        Returns stickers from the installed sticker sets that correspond to a given emoji. If the emoji is non-empty, favorite and recently used stickers may also be returned
        
        :param emoji: String representation of emoji. If empty, returns all known installed stickers
        :type emoji: :class:`str`
        
        :param limit: The maximum number of stickers to be returned
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Stickers`
        """
        _constructor = GetStickers.construct if skip_validation else GetStickers

        return await self.client.request(
            _constructor(
                emoji=emoji,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_storage_statistics(
            self,
            chat_limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StorageStatistics:
        """
        Returns storage usage statistics. Can be called before authorization
        
        :param chat_limit: The maximum number of chats with the largest storage usage for which separate statistics need to be returned. All other chats will be grouped in entries with chat_id == 0. If the chat info database is not used, the chat_limit is ignored and is always set to 0
        :type chat_limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StorageStatistics`
        """
        _constructor = GetStorageStatistics.construct if skip_validation else GetStorageStatistics

        return await self.client.request(
            _constructor(
                chat_limit=chat_limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_storage_statistics_fast(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> StorageStatisticsFast:
        """
        Quickly returns approximate storage usage statistics. Can be called before authorization
        
        """
        return await self.client.request(
            GetStorageStatisticsFast(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_suggested_file_name(
            self,
            file_id: int,
            directory: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Returns suggested name for saving a file in a given directory
        
        :param file_id: Identifier of the file
        :type file_id: :class:`int`
        
        :param directory: Directory in which the file is supposed to be saved
        :type directory: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """
        _constructor = GetSuggestedFileName.construct if skip_validation else GetSuggestedFileName

        return await self.client.request(
            _constructor(
                file_id=file_id,
                directory=directory,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_suggested_sticker_set_name(
            self,
            title: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Returns a suggested name for a new sticker set with a given title
        
        :param title: Sticker set title; 1-64 characters
        :type title: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """
        _constructor = GetSuggestedStickerSetName.construct if skip_validation else GetSuggestedStickerSetName

        return await self.client.request(
            _constructor(
                title=title,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_suitable_discussion_chats(self, *, request_id: str = None, request_timeout: int = None) -> Chats:
        """
        Returns a list of basic group and supergroup chats, which can be used as a discussion group for a channel. Returned basic group chats must be first upgraded to supergroups before they can be set as a discussion group. To set a returned supergroup as a discussion group, access to its old messages must be enabled using toggleSupergroupIsAllHistoryAvailable first
        
        """
        return await self.client.request(
            GetSuitableDiscussionChats(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_supergroup(
            self,
            supergroup_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Supergroup:
        """
        Returns information about a supergroup or a channel by its identifier. This is an offline request if the current user is not a bot
        
        :param supergroup_id: Supergroup or channel identifier
        :type supergroup_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Supergroup`
        """
        _constructor = GetSupergroup.construct if skip_validation else GetSupergroup

        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_supergroup_full_info(
            self,
            supergroup_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> SupergroupFullInfo:
        """
        Returns full information about a supergroup or a channel by its identifier, cached for up to 1 minute
        
        :param supergroup_id: Supergroup or channel identifier
        :type supergroup_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.SupergroupFullInfo`
        """
        _constructor = GetSupergroupFullInfo.construct if skip_validation else GetSupergroupFullInfo

        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_supergroup_members(
            self,
            supergroup_id: int,
            filter_: SupergroupMembersFilter,
            offset: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatMembers:
        """
        Returns information about members or banned users in a supergroup or channel. Can be used only if supergroupFullInfo.can_get_members == true; additionally, administrator privileges may be required for some filters
        
        :param supergroup_id: Identifier of the supergroup or channel
        :type supergroup_id: :class:`int`
        
        :param filter_: The type of users to return; pass null to use supergroupMembersFilterRecent
        :type filter_: :class:`SupergroupMembersFilter`
        
        :param offset: Number of users to skip
        :type offset: :class:`int`
        
        :param limit: The maximum number of users be returned; up to 200
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatMembers`
        """
        _constructor = GetSupergroupMembers.construct if skip_validation else GetSupergroupMembers

        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
                filter=filter_,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_support_user(self, *, request_id: str = None, request_timeout: int = None) -> User:
        """
        Returns a user that can be contacted to get support
        
        """
        return await self.client.request(
            GetSupportUser(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_temporary_password_state(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> TemporaryPasswordState:
        """
        Returns information about the current temporary password
        
        """
        return await self.client.request(
            GetTemporaryPasswordState(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_text_entities(
            self,
            text: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TextEntities:
        """
        Returns all entities (mentions, hashtags, cashtags, bot commands, bank card numbers, URLs, and email addresses) contained in the text. Can be called synchronously
        
        :param text: The text in which to look for entites
        :type text: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TextEntities`
        """
        _constructor = GetTextEntities.construct if skip_validation else GetTextEntities

        return await self.client.request(
            _constructor(
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_theme_parameters_json_string(
            self,
            theme: ThemeParameters,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Converts a themeParameters object to corresponding JSON-serialized string. Can be called synchronously
        
        :param theme: Theme parameters to convert to JSON
        :type theme: :class:`ThemeParameters`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """
        _constructor = GetThemeParametersJsonString.construct if skip_validation else GetThemeParametersJsonString

        return await self.client.request(
            _constructor(
                theme=theme,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_top_chats(
            self,
            category: TopChatCategory,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Returns a list of frequently used chats. Supported only if the chat info database is enabled
        
        :param category: Category of chats to be returned
        :type category: :class:`TopChatCategory`
        
        :param limit: The maximum number of chats to be returned; up to 30
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """
        _constructor = GetTopChats.construct if skip_validation else GetTopChats

        return await self.client.request(
            _constructor(
                category=category,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_trending_sticker_sets(
            self,
            offset: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSets:
        """
        Returns a list of trending sticker sets. For optimal performance, the number of returned sticker sets is chosen by TDLib
        
        :param offset: The offset from which to return the sticker sets; must be non-negative
        :type offset: :class:`int`
        
        :param limit: The maximum number of sticker sets to be returned; up to 100. For optimal performance, the number of returned sticker sets is chosen by TDLib and can be smaller than the specified limit, even if the end of the list has not been reached
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSets`
        """
        _constructor = GetTrendingStickerSets.construct if skip_validation else GetTrendingStickerSets

        return await self.client.request(
            _constructor(
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_user(
            self,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> User:
        """
        Returns information about a user by their identifier. This is an offline request if the current user is not a bot
        
        :param user_id: User identifier
        :type user_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.User`
        """
        _constructor = GetUser.construct if skip_validation else GetUser

        return await self.client.request(
            _constructor(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_user_full_info(
            self,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> UserFullInfo:
        """
        Returns full information about a user by their identifier
        
        :param user_id: User identifier
        :type user_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.UserFullInfo`
        """
        _constructor = GetUserFullInfo.construct if skip_validation else GetUserFullInfo

        return await self.client.request(
            _constructor(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_user_privacy_setting_rules(
            self,
            setting: UserPrivacySetting,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> UserPrivacySettingRules:
        """
        Returns the current privacy settings
        
        :param setting: The privacy setting
        :type setting: :class:`UserPrivacySetting`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.UserPrivacySettingRules`
        """
        _constructor = GetUserPrivacySettingRules.construct if skip_validation else GetUserPrivacySettingRules

        return await self.client.request(
            _constructor(
                setting=setting,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_user_profile_photos(
            self,
            user_id: int,
            offset: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatPhotos:
        """
        Returns the profile photos of a user. The result of this query may be outdated: some photos might have been deleted already
        
        :param user_id: User identifier
        :type user_id: :class:`int`
        
        :param offset: The number of photos to skip; must be non-negative
        :type offset: :class:`int`
        
        :param limit: The maximum number of photos to be returned; up to 100
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatPhotos`
        """
        _constructor = GetUserProfilePhotos.construct if skip_validation else GetUserProfilePhotos

        return await self.client.request(
            _constructor(
                user_id=user_id,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_video_chat_available_participants(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageSenders:
        """
        Returns list of participant identifiers, on whose behalf a video chat in the chat can be joined
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageSenders`
        """
        _constructor = GetVideoChatAvailableParticipants.construct if skip_validation else GetVideoChatAvailableParticipants

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_video_chat_rtmp_url(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> RtmpUrl:
        """
        Returns RTMP URL for streaming to the chat; requires creator privileges
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.RtmpUrl`
        """
        _constructor = GetVideoChatRtmpUrl.construct if skip_validation else GetVideoChatRtmpUrl

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_web_app_url(
            self,
            bot_user_id: int,
            url: str,
            theme: ThemeParameters,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> HttpUrl:
        """
        Returns an HTTPS URL of a web app to open after keyboardButtonTypeWebApp button is pressed
        
        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`int`
        
        :param url: The URL from the keyboardButtonTypeWebApp button
        :type url: :class:`str`
        
        :param theme: Preferred web app theme; pass null to use the default theme
        :type theme: :class:`ThemeParameters`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """
        _constructor = GetWebAppUrl.construct if skip_validation else GetWebAppUrl

        return await self.client.request(
            _constructor(
                bot_user_id=bot_user_id,
                url=url,
                theme=theme,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_web_page_instant_view(
            self,
            url: str,
            force_full: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> WebPageInstantView:
        """
        Returns an instant view version of a web page if available. Returns a 404 error if the web page has no instant view page
        
        :param url: The web page URL
        :type url: :class:`str`
        
        :param force_full: Pass true to get full instant view for the web page
        :type force_full: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.WebPageInstantView`
        """
        _constructor = GetWebPageInstantView.construct if skip_validation else GetWebPageInstantView

        return await self.client.request(
            _constructor(
                url=url,
                force_full=force_full,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_web_page_preview(
            self,
            text: FormattedText,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> WebPage:
        """
        Returns a web page preview by the text of the message. Do not call this function too often. Returns a 404 error if the web page has no preview
        
        :param text: Message text with formatting
        :type text: :class:`FormattedText`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.WebPage`
        """
        _constructor = GetWebPagePreview.construct if skip_validation else GetWebPagePreview

        return await self.client.request(
            _constructor(
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def hide_suggested_action(
            self,
            action: SuggestedAction,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Hides a suggested action
        
        :param action: Suggested action to hide
        :type action: :class:`SuggestedAction`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = HideSuggestedAction.construct if skip_validation else HideSuggestedAction

        return await self.client.request(
            _constructor(
                action=action,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def import_contacts(
            self,
            contacts: list[Contact],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ImportedContacts:
        """
        Adds new contacts or edits existing contacts by their phone numbers; contacts' user identifiers are ignored
        
        :param contacts: The list of contacts to import or edit; contacts' vCard are ignored and are not imported
        :type contacts: :class:`list[Contact]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ImportedContacts`
        """
        _constructor = ImportContacts.construct if skip_validation else ImportContacts

        return await self.client.request(
            _constructor(
                contacts=contacts,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def import_messages(
            self,
            chat_id: int,
            message_file: InputFile,
            attached_files: list[InputFile],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Imports messages exported from another app
        
        :param chat_id: Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info administrator right
        :type chat_id: :class:`int`
        
        :param message_file: File with messages to import. Only inputFileLocal and inputFileGenerated are supported. The file must not be previously uploaded
        :type message_file: :class:`InputFile`
        
        :param attached_files: Files used in the imported messages. Only inputFileLocal and inputFileGenerated are supported. The files must not be previously uploaded
        :type attached_files: :class:`list[InputFile]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ImportMessages.construct if skip_validation else ImportMessages

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_file=message_file,
                attached_files=attached_files,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def invite_group_call_participants(
            self,
            group_call_id: int,
            user_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Invites users to an active group call. Sends a service message of type messageInviteToGroupCall for video chats
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param user_ids: User identifiers. At most 10 users can be invited simultaneously
        :type user_ids: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = InviteGroupCallParticipants.construct if skip_validation else InviteGroupCallParticipants

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                user_ids=user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def join_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds the current user as a new member to a chat. Private and secret chats can't be joined using this method
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = JoinChat.construct if skip_validation else JoinChat

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def join_chat_by_invite_link(
            self,
            invite_link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Uses an invite link to add the current user to the chat if possible
        
        :param invite_link: Invite link to use
        :type invite_link: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """
        _constructor = JoinChatByInviteLink.construct if skip_validation else JoinChatByInviteLink

        return await self.client.request(
            _constructor(
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def join_group_call(
            self,
            group_call_id: int,
            participant_id: MessageSender,
            audio_source_id: int,
            payload: str,
            is_muted: bool,
            is_my_video_enabled: bool,
            invite_hash: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Joins an active group call. Returns join response payload for tgcalls
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param participant_id: Identifier of a group call participant, which will be used to join the call; pass null to join as self; video chats only
        :type participant_id: :class:`MessageSender`
        
        :param audio_source_id: Caller audio channel synchronization source identifier; received from tgcalls
        :type audio_source_id: :class:`int`
        
        :param payload: Group call join payload; received from tgcalls
        :type payload: :class:`str`
        
        :param is_muted: Pass true to join the call with muted microphone
        :type is_muted: :class:`bool`
        
        :param is_my_video_enabled: Pass true if the user's video is enabled
        :type is_my_video_enabled: :class:`bool`
        
        :param invite_hash: If non-empty, invite hash to be used to join the group call without being muted by administrators
        :type invite_hash: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """
        _constructor = JoinGroupCall.construct if skip_validation else JoinGroupCall

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                participant_id=participant_id,
                audio_source_id=audio_source_id,
                payload=payload,
                is_muted=is_muted,
                is_my_video_enabled=is_my_video_enabled,
                invite_hash=invite_hash,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def leave_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes the current user from chat members. Private and secret chats can't be left using this method
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = LeaveChat.construct if skip_validation else LeaveChat

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def leave_group_call(
            self,
            group_call_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Leaves a group call
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = LeaveGroupCall.construct if skip_validation else LeaveGroupCall

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def load_chats(
            self,
            chat_list: ChatList,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Loads more chats from a chat list. The loaded chats and their positions in the chat list will be sent through updates. Chats are sorted by the pair (chat.position.order, chat.id) in descending order. Returns a 404 error if all chats have been loaded
        
        :param chat_list: The chat list in which to load chats; pass null to load chats from the main chat list
        :type chat_list: :class:`ChatList`
        
        :param limit: The maximum number of chats to be loaded. For optimal performance, the number of loaded chats is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = LoadChats.construct if skip_validation else LoadChats

        return await self.client.request(
            _constructor(
                chat_list=chat_list,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def load_group_call_participants(
            self,
            group_call_id: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Loads more participants of a group call. The loaded participants will be received through updates. Use the field groupCall.loaded_all_participants to check whether all participants have already been loaded
        
        :param group_call_id: Group call identifier. The group call must be previously received through getGroupCall and must be joined or being joined
        :type group_call_id: :class:`int`
        
        :param limit: The maximum number of participants to load; up to 100
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = LoadGroupCallParticipants.construct if skip_validation else LoadGroupCallParticipants

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def log_out(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Closes the TDLib instance after a proper logout. Requires an available network connection. All local data will be destroyed. After the logout completes, updateAuthorizationState with authorizationStateClosed will be sent
        
        """
        return await self.client.request(
            LogOut(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def open_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs TDLib that the chat is opened by the user. Many useful activities depend on the chat being opened or closed (e.g., in supergroups and channels all updates are received only for opened chats)
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = OpenChat.construct if skip_validation else OpenChat

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def open_message_content(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs TDLib that the message content has been opened (e.g., the user has opened a photo, video, document, location or venue, or has listened to an audio file or voice note message). An updateMessageContentOpened update will be generated if something has changed
        
        :param chat_id: Chat identifier of the message
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message with the opened content
        :type message_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = OpenMessageContent.construct if skip_validation else OpenMessageContent

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def open_web_app(
            self,
            chat_id: int,
            bot_user_id: int,
            url: str,
            theme: ThemeParameters,
            reply_to_message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> WebAppInfo:
        """
        Informs TDLib that a web app is being opened from attachment menu, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an inlineKeyboardButtonTypeWebApp button. For each bot, a confirmation alert about data sent to the bot must be shown once
        
        :param chat_id: Identifier of the chat in which the web app is opened. Web apps can be opened only in private chats for now
        :type chat_id: :class:`int`
        
        :param bot_user_id: Identifier of the bot, providing the web app
        :type bot_user_id: :class:`int`
        
        :param url: The URL from an inlineKeyboardButtonTypeWebApp button, a botMenuButton button, or an internalLinkTypeAttachmentMenuBot link, or an empty string otherwise
        :type url: :class:`str`
        
        :param theme: Preferred web app theme; pass null to use the default theme
        :type theme: :class:`ThemeParameters`
        
        :param reply_to_message_id: Identifier of the replied message for the message sent by the web app; 0 if none
        :type reply_to_message_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.WebAppInfo`
        """
        _constructor = OpenWebApp.construct if skip_validation else OpenWebApp

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                bot_user_id=bot_user_id,
                url=url,
                theme=theme,
                reply_to_message_id=reply_to_message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def optimize_storage(
            self,
            size: int,
            ttl: int,
            count: int,
            immunity_delay: int,
            file_types: list[FileType],
            chat_ids: list[int],
            exclude_chat_ids: list[int],
            return_deleted_file_statistics: bool,
            chat_limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StorageStatistics:
        """
        Optimizes storage usage, i.e. deletes some files and returns new storage usage statistics. Secret thumbnails can't be deleted
        
        :param size: Limit on the total size of files after deletion, in bytes. Pass -1 to use the default limit
        :type size: :class:`int`
        
        :param ttl: Limit on the time that has passed since the last time a file was accessed (or creation time for some filesystems). Pass -1 to use the default limit
        :type ttl: :class:`int`
        
        :param count: Limit on the total number of files after deletion. Pass -1 to use the default limit
        :type count: :class:`int`
        
        :param immunity_delay: The amount of time after the creation of a file during which it can't be deleted, in seconds. Pass -1 to use the default value
        :type immunity_delay: :class:`int`
        
        :param file_types: If non-empty, only files with the given types are considered. By default, all types except thumbnails, profile photos, stickers and wallpapers are deleted
        :type file_types: :class:`list[FileType]`
        
        :param chat_ids: If non-empty, only files from the given chats are considered. Use 0 as chat identifier to delete files not belonging to any chat (e.g., profile photos)
        :type chat_ids: :class:`list[int]`
        
        :param exclude_chat_ids: If non-empty, files from the given chats are excluded. Use 0 as chat identifier to exclude all files not belonging to any chat (e.g., profile photos)
        :type exclude_chat_ids: :class:`list[int]`
        
        :param return_deleted_file_statistics: Pass true if statistics about the files that were deleted must be returned instead of the whole storage usage statistics. Affects only returned statistics
        :type return_deleted_file_statistics: :class:`bool`
        
        :param chat_limit: Same as in getStorageStatistics. Affects only returned statistics
        :type chat_limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StorageStatistics`
        """
        _constructor = OptimizeStorage.construct if skip_validation else OptimizeStorage

        return await self.client.request(
            _constructor(
                size=size,
                ttl=ttl,
                count=count,
                immunity_delay=immunity_delay,
                file_types=file_types,
                chat_ids=chat_ids,
                exclude_chat_ids=exclude_chat_ids,
                return_deleted_file_statistics=return_deleted_file_statistics,
                chat_limit=chat_limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def parse_markdown(
            self,
            text: FormattedText,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FormattedText:
        """
        Parses Markdown entities in a human-friendly format, ignoring markup errors. Can be called synchronously
        
        :param text: The text to parse. For example, "__italic__ ~~strikethrough~~ ||spoiler|| **bold** `code` ```pre``` __[italic__ text_url](telegram.org) __italic**bold italic__bold**"
        :type text: :class:`FormattedText`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FormattedText`
        """
        _constructor = ParseMarkdown.construct if skip_validation else ParseMarkdown

        return await self.client.request(
            _constructor(
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def parse_text_entities(
            self,
            text: str,
            parse_mode: TextParseMode,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FormattedText:
        """
        Parses Bold, Italic, Underline, Strikethrough, Spoiler, Code, Pre, PreCode, TextUrl and MentionName entities contained in the text. Can be called synchronously
        
        :param text: The text to parse
        :type text: :class:`str`
        
        :param parse_mode: Text parse mode
        :type parse_mode: :class:`TextParseMode`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FormattedText`
        """
        _constructor = ParseTextEntities.construct if skip_validation else ParseTextEntities

        return await self.client.request(
            _constructor(
                text=text,
                parse_mode=parse_mode,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def pin_chat_message(
            self,
            chat_id: int,
            message_id: int,
            disable_notification: bool,
            only_for_self: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Pins a message in a chat; requires can_pin_messages rights or can_edit_messages rights in the channel
        
        :param chat_id: Identifier of the chat
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the new pinned message
        :type message_id: :class:`int`
        
        :param disable_notification: Pass true to disable notification about the pinned message. Notifications are always disabled in channels and private chats
        :type disable_notification: :class:`bool`
        
        :param only_for_self: Pass true to pin the message only for self; private chats only
        :type only_for_self: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = PinChatMessage.construct if skip_validation else PinChatMessage

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                disable_notification=disable_notification,
                only_for_self=only_for_self,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def ping_proxy(
            self,
            proxy_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Seconds:
        """
        Computes time needed to receive a response from a Telegram server through a proxy. Can be called before authorization
        
        :param proxy_id: Proxy identifier. Use 0 to ping a Telegram server without a proxy
        :type proxy_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Seconds`
        """
        _constructor = PingProxy.construct if skip_validation else PingProxy

        return await self.client.request(
            _constructor(
                proxy_id=proxy_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def process_chat_join_request(
            self,
            chat_id: int,
            user_id: int,
            approve: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Handles a pending join request in a chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param user_id: Identifier of the user that sent the request
        :type user_id: :class:`int`
        
        :param approve: Pass true to approve the request; pass false to decline it
        :type approve: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ProcessChatJoinRequest.construct if skip_validation else ProcessChatJoinRequest

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                user_id=user_id,
                approve=approve,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def process_chat_join_requests(
            self,
            chat_id: int,
            invite_link: str,
            approve: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Handles all pending join requests for a given link in a chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param invite_link: Invite link for which to process join requests. If empty, all join requests will be processed. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        :type invite_link: :class:`str`
        
        :param approve: Pass true to approve all requests; pass false to decline them
        :type approve: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ProcessChatJoinRequests.construct if skip_validation else ProcessChatJoinRequests

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                invite_link=invite_link,
                approve=approve,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def process_push_notification(
            self,
            payload: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Handles a push notification. Returns error with code 406 if the push notification is not supported and connection to the server is required to fetch new data. Can be called before authorization
        
        :param payload: JSON-encoded push notification payload with all fields sent by the server, and "google.sent_time" and "google.notification.sound" fields added
        :type payload: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ProcessPushNotification.construct if skip_validation else ProcessPushNotification

        return await self.client.request(
            _constructor(
                payload=payload,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def read_all_chat_mentions(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Marks all mentions in a chat as read
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ReadAllChatMentions.construct if skip_validation else ReadAllChatMentions

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def read_all_chat_reactions(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Marks all reactions in a chat as read
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ReadAllChatReactions.construct if skip_validation else ReadAllChatReactions

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def read_file_part(
            self,
            file_id: int,
            offset: int,
            count: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FilePart:
        """
        Reads a part of a file from the TDLib file cache and returns read bytes. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct read from the file
        
        :param file_id: Identifier of the file. The file must be located in the TDLib file cache
        :type file_id: :class:`int`
        
        :param offset: The offset from which to read the file
        :type offset: :class:`int`
        
        :param count: Number of bytes to read. An error will be returned if there are not enough bytes available in the file from the specified position. Pass 0 to read all available data from the specified position
        :type count: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FilePart`
        """
        _constructor = ReadFilePart.construct if skip_validation else ReadFilePart

        return await self.client.request(
            _constructor(
                file_id=file_id,
                offset=offset,
                count=count,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def recover_authentication_password(
            self,
            recovery_code: str,
            new_password: str,
            new_hint: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Recovers the password with a password recovery code sent to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword
        
        :param recovery_code: Recovery code to check
        :type recovery_code: :class:`str`
        
        :param new_password: New password of the user; may be empty to remove the password
        :type new_password: :class:`str`
        
        :param new_hint: New password hint; may be empty
        :type new_hint: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RecoverAuthenticationPassword.construct if skip_validation else RecoverAuthenticationPassword

        return await self.client.request(
            _constructor(
                recovery_code=recovery_code,
                new_password=new_password,
                new_hint=new_hint,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def recover_password(
            self,
            recovery_code: str,
            new_password: str,
            new_hint: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PasswordState:
        """
        Recovers the 2-step verification password using a recovery code sent to an email address that was previously set up
        
        :param recovery_code: Recovery code to check
        :type recovery_code: :class:`str`
        
        :param new_password: New password of the user; may be empty to remove the password
        :type new_password: :class:`str`
        
        :param new_hint: New password hint; may be empty
        :type new_hint: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PasswordState`
        """
        _constructor = RecoverPassword.construct if skip_validation else RecoverPassword

        return await self.client.request(
            _constructor(
                recovery_code=recovery_code,
                new_password=new_password,
                new_hint=new_hint,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def register_device(
            self,
            device_token: DeviceToken,
            other_user_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PushReceiverId:
        """
        Registers the currently used device for receiving push notifications. Returns a globally unique identifier of the push notification subscription
        
        :param device_token: Device token
        :type device_token: :class:`DeviceToken`
        
        :param other_user_ids: List of user identifiers of other users currently using the application
        :type other_user_ids: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PushReceiverId`
        """
        _constructor = RegisterDevice.construct if skip_validation else RegisterDevice

        return await self.client.request(
            _constructor(
                device_token=device_token,
                other_user_ids=other_user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def register_user(
            self,
            first_name: str,
            last_name: typing.Optional[str],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Finishes user registration. Works only when the current authorization state is authorizationStateWaitRegistration
        
        :param first_name: The first name of the user; 1-64 characters
        :type first_name: :class:`str`
        
        :param last_name: The last name of the user; 0-64 characters, defaults to None
        :type last_name: :class:`str`, optional
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RegisterUser.construct if skip_validation else RegisterUser

        return await self.client.request(
            _constructor(
                first_name=first_name,
                last_name=last_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_all_files_from_downloads(
            self,
            only_active: bool,
            only_completed: bool,
            delete_from_cache: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes all files from the file download list
        
        :param only_active: Pass true to remove only active downloads, including paused
        :type only_active: :class:`bool`
        
        :param only_completed: Pass true to remove only completed downloads
        :type only_completed: :class:`bool`
        
        :param delete_from_cache: Pass true to delete the file from the TDLib file cache
        :type delete_from_cache: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveAllFilesFromDownloads.construct if skip_validation else RemoveAllFilesFromDownloads

        return await self.client.request(
            _constructor(
                only_active=only_active,
                only_completed=only_completed,
                delete_from_cache=delete_from_cache,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_background(
            self,
            background_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes background from the list of installed backgrounds
        
        :param background_id: The background identifier
        :type background_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveBackground.construct if skip_validation else RemoveBackground

        return await self.client.request(
            _constructor(
                background_id=background_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_chat_action_bar(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a chat action bar without any other action
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveChatActionBar.construct if skip_validation else RemoveChatActionBar

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_contacts(
            self,
            user_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes users from the contact list
        
        :param user_ids: Identifiers of users to be deleted
        :type user_ids: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveContacts.construct if skip_validation else RemoveContacts

        return await self.client.request(
            _constructor(
                user_ids=user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_favorite_sticker(
            self,
            sticker: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a sticker from the list of favorite stickers
        
        :param sticker: Sticker file to delete from the list
        :type sticker: :class:`InputFile`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveFavoriteSticker.construct if skip_validation else RemoveFavoriteSticker

        return await self.client.request(
            _constructor(
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_file_from_downloads(
            self,
            file_id: int,
            delete_from_cache: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a file from the file download list
        
        :param file_id: Identifier of the downloaded file
        :type file_id: :class:`int`
        
        :param delete_from_cache: Pass true to delete the file from the TDLib file cache
        :type delete_from_cache: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveFileFromDownloads.construct if skip_validation else RemoveFileFromDownloads

        return await self.client.request(
            _constructor(
                file_id=file_id,
                delete_from_cache=delete_from_cache,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_notification(
            self,
            notification_group_id: int,
            notification_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes an active notification from notification list. Needs to be called only if the notification is removed by the current user
        
        :param notification_group_id: Identifier of notification group to which the notification belongs
        :type notification_group_id: :class:`int`
        
        :param notification_id: Identifier of removed notification
        :type notification_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveNotification.construct if skip_validation else RemoveNotification

        return await self.client.request(
            _constructor(
                notification_group_id=notification_group_id,
                notification_id=notification_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_notification_group(
            self,
            notification_group_id: int,
            max_notification_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a group of active notifications. Needs to be called only if the notification group is removed by the current user
        
        :param notification_group_id: Notification group identifier
        :type notification_group_id: :class:`int`
        
        :param max_notification_id: The maximum identifier of removed notifications
        :type max_notification_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveNotificationGroup.construct if skip_validation else RemoveNotificationGroup

        return await self.client.request(
            _constructor(
                notification_group_id=notification_group_id,
                max_notification_id=max_notification_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_proxy(
            self,
            proxy_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a proxy server. Can be called before authorization
        
        :param proxy_id: Proxy identifier
        :type proxy_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveProxy.construct if skip_validation else RemoveProxy

        return await self.client.request(
            _constructor(
                proxy_id=proxy_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_recent_hashtag(
            self,
            hashtag: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a hashtag from the list of recently used hashtags
        
        :param hashtag: Hashtag to delete
        :type hashtag: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveRecentHashtag.construct if skip_validation else RemoveRecentHashtag

        return await self.client.request(
            _constructor(
                hashtag=hashtag,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_recent_sticker(
            self,
            is_attached: bool,
            sticker: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a sticker from the list of recently used stickers
        
        :param is_attached: Pass true to remove the sticker from the list of stickers recently attached to photo or video files; pass false to remove the sticker from the list of recently sent stickers
        :type is_attached: :class:`bool`
        
        :param sticker: Sticker file to delete
        :type sticker: :class:`InputFile`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveRecentSticker.construct if skip_validation else RemoveRecentSticker

        return await self.client.request(
            _constructor(
                is_attached=is_attached,
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_recently_found_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a chat from the list of recently found chats
        
        :param chat_id: Identifier of the chat to be removed
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveRecentlyFoundChat.construct if skip_validation else RemoveRecentlyFoundChat

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_saved_animation(
            self,
            animation: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes an animation from the list of saved animations
        
        :param animation: Animation file to be removed
        :type animation: :class:`InputFile`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveSavedAnimation.construct if skip_validation else RemoveSavedAnimation

        return await self.client.request(
            _constructor(
                animation=animation,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_saved_notification_sound(
            self,
            notification_sound_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a notification sound from the list of saved notification sounds
        
        :param notification_sound_id: Identifier of the notification sound
        :type notification_sound_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveSavedNotificationSound.construct if skip_validation else RemoveSavedNotificationSound

        return await self.client.request(
            _constructor(
                notification_sound_id=notification_sound_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_sticker_from_set(
            self,
            sticker: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a sticker from the set to which it belongs; for bots only. The sticker set must have been created by the bot
        
        :param sticker: Sticker
        :type sticker: :class:`InputFile`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveStickerFromSet.construct if skip_validation else RemoveStickerFromSet

        return await self.client.request(
            _constructor(
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_top_chat(
            self,
            category: TopChatCategory,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a chat from the list of frequently used chats. Supported only if the chat info database is enabled
        
        :param category: Category of frequently used chats
        :type category: :class:`TopChatCategory`
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RemoveTopChat.construct if skip_validation else RemoveTopChat

        return await self.client.request(
            _constructor(
                category=category,
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reorder_chat_filters(
            self,
            chat_filter_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the order of chat filters
        
        :param chat_filter_ids: Identifiers of chat filters in the new correct order
        :type chat_filter_ids: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ReorderChatFilters.construct if skip_validation else ReorderChatFilters

        return await self.client.request(
            _constructor(
                chat_filter_ids=chat_filter_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reorder_installed_sticker_sets(
            self,
            is_masks: bool,
            sticker_set_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the order of installed sticker sets
        
        :param is_masks: Pass true to change the order of mask sticker sets; pass false to change the order of ordinary sticker sets
        :type is_masks: :class:`bool`
        
        :param sticker_set_ids: Identifiers of installed sticker sets in the new correct order
        :type sticker_set_ids: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ReorderInstalledStickerSets.construct if skip_validation else ReorderInstalledStickerSets

        return await self.client.request(
            _constructor(
                is_masks=is_masks,
                sticker_set_ids=sticker_set_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def replace_primary_chat_invite_link(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLink:
        """
        Replaces current primary invite link for a chat with a new primary invite link. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLink`
        """
        _constructor = ReplacePrimaryChatInviteLink.construct if skip_validation else ReplacePrimaryChatInviteLink

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def replace_video_chat_rtmp_url(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> RtmpUrl:
        """
        Replaces the current RTMP URL for streaming to the chat; requires creator privileges
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.RtmpUrl`
        """
        _constructor = ReplaceVideoChatRtmpUrl.construct if skip_validation else ReplaceVideoChatRtmpUrl

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def report_chat(
            self,
            chat_id: int,
            message_ids: list[int],
            reason: ChatReportReason,
            text: typing.Optional[str],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if chat.can_be_reported
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param message_ids: Identifiers of reported messages; may be empty to report the whole chat
        :type message_ids: :class:`list[int]`
        
        :param reason: The reason for reporting the chat
        :type reason: :class:`ChatReportReason`
        
        :param text: Additional report details; 0-1024 characters, defaults to None
        :type text: :class:`str`, optional
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ReportChat.construct if skip_validation else ReportChat

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_ids=message_ids,
                reason=reason,
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def report_chat_photo(
            self,
            chat_id: int,
            file_id: int,
            reason: ChatReportReason,
            text: typing.Optional[str],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Reports a chat photo to the Telegram moderators. A chat photo can be reported only if chat.can_be_reported
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param file_id: Identifier of the photo to report. Only full photos from chatPhoto can be reported
        :type file_id: :class:`int`
        
        :param reason: The reason for reporting the chat photo
        :type reason: :class:`ChatReportReason`
        
        :param text: Additional report details; 0-1024 characters, defaults to None
        :type text: :class:`str`, optional
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ReportChatPhoto.construct if skip_validation else ReportChatPhoto

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                file_id=file_id,
                reason=reason,
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def report_supergroup_spam(
            self,
            supergroup_id: int,
            message_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Reports messages in a supergroup as spam; requires administrator rights in the supergroup
        
        :param supergroup_id: Supergroup identifier
        :type supergroup_id: :class:`int`
        
        :param message_ids: Identifiers of messages to report
        :type message_ids: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ReportSupergroupSpam.construct if skip_validation else ReportSupergroupSpam

        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
                message_ids=message_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def request_authentication_password_recovery(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> Ok:
        """
        Requests to send a password recovery code to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword
        
        """
        return await self.client.request(
            RequestAuthenticationPasswordRecovery(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def request_password_recovery(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> EmailAddressAuthenticationCodeInfo:
        """
        Requests to send a 2-step verification password recovery code to an email address that was previously set up
        
        """
        return await self.client.request(
            RequestPasswordRecovery(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def request_qr_code_authentication(
            self,
            other_user_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Requests QR code authentication by scanning a QR code on another logged in device. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword
        
        :param other_user_ids: List of user identifiers of other users currently using the application
        :type other_user_ids: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RequestQrCodeAuthentication.construct if skip_validation else RequestQrCodeAuthentication

        return await self.client.request(
            _constructor(
                other_user_ids=other_user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_authentication_code(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Re-sends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitCode, the next_code_type of the result is not null and the server-specified timeout has passed
        
        """
        return await self.client.request(
            ResendAuthenticationCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_change_phone_number_code(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> AuthenticationCodeInfo:
        """
        Re-sends the authentication code sent to confirm a new phone number for the current user. Works only if the previously received authenticationCodeInfo next_code_type was not null and the server-specified timeout has passed
        
        """
        return await self.client.request(
            ResendChangePhoneNumberCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_email_address_verification_code(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> EmailAddressAuthenticationCodeInfo:
        """
        Re-sends the code to verify an email address to be added to a user's Telegram Passport
        
        """
        return await self.client.request(
            ResendEmailAddressVerificationCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_messages(
            self,
            chat_id: int,
            message_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Resends messages which failed to send. Can be called only for messages for which messageSendingStateFailed.can_retry is true and after specified in messageSendingStateFailed.retry_after time passed. If a message is re-sent, the corresponding failed to send message is deleted. Returns the sent messages in the same order as the message identifiers passed in message_ids. If a message can't be re-sent, null will be returned instead of the message
        
        :param chat_id: Identifier of the chat to send messages
        :type chat_id: :class:`int`
        
        :param message_ids: Identifiers of the messages to resend. Message identifiers must be in a strictly increasing order
        :type message_ids: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """
        _constructor = ResendMessages.construct if skip_validation else ResendMessages

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_ids=message_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_phone_number_confirmation_code(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> AuthenticationCodeInfo:
        """
        Resends phone number confirmation code
        
        """
        return await self.client.request(
            ResendPhoneNumberConfirmationCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_phone_number_verification_code(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> AuthenticationCodeInfo:
        """
        Re-sends the code to verify a phone number to be added to a user's Telegram Passport
        
        """
        return await self.client.request(
            ResendPhoneNumberVerificationCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_recovery_email_address_code(
            self,
            *,
            request_id: str = None,
            request_timeout: int = None
            ) -> PasswordState:
        """
        Resends the 2-step verification recovery email address verification code
        
        """
        return await self.client.request(
            ResendRecoveryEmailAddressCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reset_all_notification_settings(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Resets all notification settings to their default values. By default, all chats are unmuted and message previews are shown
        
        """
        return await self.client.request(
            ResetAllNotificationSettings(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reset_backgrounds(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Resets list of installed backgrounds to its default value
        
        """
        return await self.client.request(
            ResetBackgrounds(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reset_network_statistics(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Resets all network data usage statistics to zero. Can be called before authorization
        
        """
        return await self.client.request(
            ResetNetworkStatistics(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reset_password(self, *, request_id: str = None, request_timeout: int = None) -> ResetPasswordResult:
        """
        Removes 2-step verification password without previous password and access to recovery email address. The password can't be reset immediately and the request needs to be repeated after the specified time
        
        """
        return await self.client.request(
            ResetPassword(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def revoke_chat_invite_link(
            self,
            chat_id: int,
            invite_link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLinks:
        """
        Revokes invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links. If a primary link is revoked, then additionally to the revoked link returns new primary link
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param invite_link: Invite link to be revoked
        :type invite_link: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLinks`
        """
        _constructor = RevokeChatInviteLink.construct if skip_validation else RevokeChatInviteLink

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def revoke_group_call_invite_link(
            self,
            group_call_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Revokes invite link for a group call. Requires groupCall.can_be_managed group call flag
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = RevokeGroupCallInviteLink.construct if skip_validation else RevokeGroupCallInviteLink

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def save_application_log_event(
            self,
            type_: str,
            chat_id: int,
            data: JsonValue,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Saves application log event on the server. Can be called before authorization
        
        :param type_: Event type
        :type type_: :class:`str`
        
        :param chat_id: Optional chat identifier, associated with the event
        :type chat_id: :class:`int`
        
        :param data: The log event data
        :type data: :class:`JsonValue`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SaveApplicationLogEvent.construct if skip_validation else SaveApplicationLogEvent

        return await self.client.request(
            _constructor(
                type=type_,
                chat_id=chat_id,
                data=data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_background(
            self,
            name: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Background:
        """
        Searches for a background by its name
        
        :param name: The name of the background
        :type name: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Background`
        """
        _constructor = SearchBackground.construct if skip_validation else SearchBackground

        return await self.client.request(
            _constructor(
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_call_messages(
            self,
            from_message_id: int,
            limit: int,
            only_missed: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Searches for call messages. Returns the results in reverse chronological order (i. e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib
        
        :param from_message_id: Identifier of the message from which to search; use 0 to get results from the last message
        :type from_message_id: :class:`int`
        
        :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`int`
        
        :param only_missed: Pass true to search only for messages with missed/declined calls
        :type only_missed: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """
        _constructor = SearchCallMessages.construct if skip_validation else SearchCallMessages

        return await self.client.request(
            _constructor(
                from_message_id=from_message_id,
                limit=limit,
                only_missed=only_missed,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_chat_members(
            self,
            chat_id: int,
            query: str,
            limit: int,
            filter_: ChatMembersFilter,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatMembers:
        """
        Searches for a specified query in the first name, last name and username of the members of a specified chat. Requires administrator rights in channels
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param query: Query to search for
        :type query: :class:`str`
        
        :param limit: The maximum number of users to be returned; up to 200
        :type limit: :class:`int`
        
        :param filter_: The type of users to search for; pass null to search among all chat members
        :type filter_: :class:`ChatMembersFilter`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatMembers`
        """
        _constructor = SearchChatMembers.construct if skip_validation else SearchChatMembers

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                query=query,
                limit=limit,
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_chat_messages(
            self,
            chat_id: int,
            query: str,
            sender_id: MessageSender,
            from_message_id: int,
            offset: int,
            limit: int,
            filter_: SearchMessagesFilter,
            message_thread_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Searches for messages with given words in the chat. Returns the results in reverse chronological order, i.e. in order of decreasing message_id. Cannot be used in secret chats with a non-empty query (searchSecretMessages must be used instead), or without an enabled message database. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        
        :param chat_id: Identifier of the chat in which to search messages
        :type chat_id: :class:`int`
        
        :param query: Query to search for
        :type query: :class:`str`
        
        :param sender_id: Identifier of the sender of messages to search for; pass null to search for messages from any sender. Not supported in secret chats
        :type sender_id: :class:`MessageSender`
        
        :param from_message_id: Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        :type from_message_id: :class:`int`
        
        :param offset: Specify 0 to get results from exactly the from_message_id or a negative offset to get the specified message and some newer messages
        :type offset: :class:`int`
        
        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than -offset. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`int`
        
        :param filter_: Additional filter for messages to search; pass null to search for all messages
        :type filter_: :class:`SearchMessagesFilter`
        
        :param message_thread_id: If not 0, only messages in the specified thread will be returned; supergroups only
        :type message_thread_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """
        _constructor = SearchChatMessages.construct if skip_validation else SearchChatMessages

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                query=query,
                sender_id=sender_id,
                from_message_id=from_message_id,
                offset=offset,
                limit=limit,
                filter=filter_,
                message_thread_id=message_thread_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_chat_recent_location_messages(
            self,
            chat_id: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Returns information about the recent locations of chat members that were sent to the chat. Returns up to 1 location message per user
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param limit: The maximum number of messages to be returned
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """
        _constructor = SearchChatRecentLocationMessages.construct if skip_validation else SearchChatRecentLocationMessages

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_chats(
            self,
            query: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Searches for the specified query in the title and username of already known chats, this is an offline request. Returns chats in the order seen in the main chat list
        
        :param query: Query to search for. If the query is empty, returns up to 50 recently found chats
        :type query: :class:`str`
        
        :param limit: The maximum number of chats to be returned
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """
        _constructor = SearchChats.construct if skip_validation else SearchChats

        return await self.client.request(
            _constructor(
                query=query,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_chats_nearby(
            self,
            location: Location,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatsNearby:
        """
        Returns a list of users and location-based supergroups nearby. The list of users nearby will be updated for 60 seconds after the request by the updates updateUsersNearby. The request must be sent again every 25 seconds with adjusted location to not miss new chats
        
        :param location: Current user location
        :type location: :class:`Location`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatsNearby`
        """
        _constructor = SearchChatsNearby.construct if skip_validation else SearchChatsNearby

        return await self.client.request(
            _constructor(
                location=location,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_chats_on_server(
            self,
            query: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Searches for the specified query in the title and username of already known chats via request to the server. Returns chats in the order seen in the main chat list
        
        :param query: Query to search for
        :type query: :class:`str`
        
        :param limit: The maximum number of chats to be returned
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """
        _constructor = SearchChatsOnServer.construct if skip_validation else SearchChatsOnServer

        return await self.client.request(
            _constructor(
                query=query,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_contacts(
            self,
            query: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Users:
        """
        Searches for the specified query in the first names, last names and usernames of the known user contacts
        
        :param query: Query to search for; may be empty to return all contacts
        :type query: :class:`str`
        
        :param limit: The maximum number of users to be returned
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Users`
        """
        _constructor = SearchContacts.construct if skip_validation else SearchContacts

        return await self.client.request(
            _constructor(
                query=query,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_emojis(
            self,
            text: str,
            exact_match: bool,
            input_language_codes: list[str],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Emojis:
        """
        Searches for emojis by keywords. Supported only if the file database is enabled
        
        :param text: Text to search for
        :type text: :class:`str`
        
        :param exact_match: Pass true if only emojis, which exactly match the text, needs to be returned
        :type exact_match: :class:`bool`
        
        :param input_language_codes: List of possible IETF language tags of the user's input language; may be empty if unknown
        :type input_language_codes: :class:`list[str]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Emojis`
        """
        _constructor = SearchEmojis.construct if skip_validation else SearchEmojis

        return await self.client.request(
            _constructor(
                text=text,
                exact_match=exact_match,
                input_language_codes=input_language_codes,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_file_downloads(
            self,
            query: str,
            only_active: bool,
            only_completed: bool,
            offset: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FoundFileDownloads:
        """
        Searches for files in the file download list or recently downloaded files from the list
        
        :param query: Query to search for; may be empty to return all downloaded files
        :type query: :class:`str`
        
        :param only_active: Pass true to search only for active downloads, including paused
        :type only_active: :class:`bool`
        
        :param only_completed: Pass true to search only for completed downloads
        :type only_completed: :class:`bool`
        
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :type offset: :class:`str`
        
        :param limit: The maximum number of files to be returned
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FoundFileDownloads`
        """
        _constructor = SearchFileDownloads.construct if skip_validation else SearchFileDownloads

        return await self.client.request(
            _constructor(
                query=query,
                only_active=only_active,
                only_completed=only_completed,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_hashtags(
            self,
            prefix: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Hashtags:
        """
        Searches for recently used hashtags by their prefix
        
        :param prefix: Hashtag prefix to search for
        :type prefix: :class:`str`
        
        :param limit: The maximum number of hashtags to be returned
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Hashtags`
        """
        _constructor = SearchHashtags.construct if skip_validation else SearchHashtags

        return await self.client.request(
            _constructor(
                prefix=prefix,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_installed_sticker_sets(
            self,
            is_masks: bool,
            query: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSets:
        """
        Searches for installed sticker sets by looking for specified query in their title and name
        
        :param is_masks: Pass true to return mask sticker sets; pass false to return ordinary sticker sets
        :type is_masks: :class:`bool`
        
        :param query: Query to search for
        :type query: :class:`str`
        
        :param limit: The maximum number of sticker sets to return
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSets`
        """
        _constructor = SearchInstalledStickerSets.construct if skip_validation else SearchInstalledStickerSets

        return await self.client.request(
            _constructor(
                is_masks=is_masks,
                query=query,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_messages(
            self,
            chat_list: ChatList,
            query: str,
            offset_date: int,
            offset_chat_id: int,
            offset_message_id: int,
            limit: int,
            filter_: SearchMessagesFilter,
            min_date: int,
            max_date: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Searches for messages in all chats except secret chats. Returns the results in reverse chronological order (i.e., in order of decreasing (date, chat_id, message_id)). For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        
        :param chat_list: Chat list in which to search messages; pass null to search in all chats regardless of their chat list. Only Main and Archive chat lists are supported
        :type chat_list: :class:`ChatList`
        
        :param query: Query to search for
        :type query: :class:`str`
        
        :param offset_date: The date of the message starting from which the results need to be fetched. Use 0 or any date in the future to get results from the last message
        :type offset_date: :class:`int`
        
        :param offset_chat_id: The chat identifier of the last found message, or 0 for the first request
        :type offset_chat_id: :class:`int`
        
        :param offset_message_id: The message identifier of the last found message, or 0 for the first request
        :type offset_message_id: :class:`int`
        
        :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`int`
        
        :param filter_: Additional filter for messages to search; pass null to search for all messages. Filters searchMessagesFilterMention, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, searchMessagesFilterFailedToSend, and searchMessagesFilterPinned are unsupported in this function
        :type filter_: :class:`SearchMessagesFilter`
        
        :param min_date: If not 0, the minimum date of the messages to return
        :type min_date: :class:`int`
        
        :param max_date: If not 0, the maximum date of the messages to return
        :type max_date: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """
        _constructor = SearchMessages.construct if skip_validation else SearchMessages

        return await self.client.request(
            _constructor(
                chat_list=chat_list,
                query=query,
                offset_date=offset_date,
                offset_chat_id=offset_chat_id,
                offset_message_id=offset_message_id,
                limit=limit,
                filter=filter_,
                min_date=min_date,
                max_date=max_date,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_outgoing_document_messages(
            self,
            query: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FoundMessages:
        """
        Searches for outgoing messages with content of the type messageDocument in all chats except secret chats. Returns the results in reverse chronological order
        
        :param query: Query to search for in document file name and message caption
        :type query: :class:`str`
        
        :param limit: The maximum number of messages to be returned; up to 100
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FoundMessages`
        """
        _constructor = SearchOutgoingDocumentMessages.construct if skip_validation else SearchOutgoingDocumentMessages

        return await self.client.request(
            _constructor(
                query=query,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_public_chat(
            self,
            username: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Searches a public chat by its username. Currently, only private chats, supergroups and channels can be public. Returns the chat if found; otherwise an error is returned
        
        :param username: Username to be resolved
        :type username: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """
        _constructor = SearchPublicChat.construct if skip_validation else SearchPublicChat

        return await self.client.request(
            _constructor(
                username=username,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_public_chats(
            self,
            query: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Searches public chats by looking for specified query in their username and title. Currently, only private chats, supergroups and channels can be public. Returns a meaningful number of results. Excludes private chats with contacts and chats from the chat list from the results
        
        :param query: Query to search for
        :type query: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """
        _constructor = SearchPublicChats.construct if skip_validation else SearchPublicChats

        return await self.client.request(
            _constructor(
                query=query,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_secret_messages(
            self,
            chat_id: int,
            query: str,
            offset: str,
            limit: int,
            filter_: SearchMessagesFilter,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FoundMessages:
        """
        Searches for messages in secret chats. Returns the results in reverse chronological order. For optimal performance, the number of returned messages is chosen by TDLib
        
        :param chat_id: Identifier of the chat in which to search. Specify 0 to search in all secret chats
        :type chat_id: :class:`int`
        
        :param query: Query to search for. If empty, searchChatMessages must be used instead
        :type query: :class:`str`
        
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :type offset: :class:`str`
        
        :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`int`
        
        :param filter_: Additional filter for messages to search; pass null to search for all messages
        :type filter_: :class:`SearchMessagesFilter`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FoundMessages`
        """
        _constructor = SearchSecretMessages.construct if skip_validation else SearchSecretMessages

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                query=query,
                offset=offset,
                limit=limit,
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_sticker_set(
            self,
            name: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSet:
        """
        Searches for a sticker set by its name
        
        :param name: Name of the sticker set
        :type name: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSet`
        """
        _constructor = SearchStickerSet.construct if skip_validation else SearchStickerSet

        return await self.client.request(
            _constructor(
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_sticker_sets(
            self,
            query: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSets:
        """
        Searches for ordinary sticker sets by looking for specified query in their title and name. Excludes installed sticker sets from the results
        
        :param query: Query to search for
        :type query: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSets`
        """
        _constructor = SearchStickerSets.construct if skip_validation else SearchStickerSets

        return await self.client.request(
            _constructor(
                query=query,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_stickers(
            self,
            emoji: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Stickers:
        """
        Searches for stickers from public sticker sets that correspond to a given emoji
        
        :param emoji: String representation of emoji; must be non-empty
        :type emoji: :class:`str`
        
        :param limit: The maximum number of stickers to be returned
        :type limit: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Stickers`
        """
        _constructor = SearchStickers.construct if skip_validation else SearchStickers

        return await self.client.request(
            _constructor(
                emoji=emoji,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_user_by_phone_number(
            self,
            phone_number: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> User:
        """
        Searches a user by their phone number
        
        :param phone_number: Phone number to search for
        :type phone_number: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.User`
        """
        _constructor = SearchUserByPhoneNumber.construct if skip_validation else SearchUserByPhoneNumber

        return await self.client.request(
            _constructor(
                phone_number=phone_number,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_bot_start_message(
            self,
            bot_user_id: int,
            chat_id: int,
            parameter: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Invites a bot to a chat (if it is not yet a member) and sends it the /start command. Bots can't be invited to a private chat other than the chat with the bot. Bots can't be invited to channels (although they can be added as admins) and secret chats. Returns the sent message
        
        :param bot_user_id: Identifier of the bot
        :type bot_user_id: :class:`int`
        
        :param chat_id: Identifier of the target chat
        :type chat_id: :class:`int`
        
        :param parameter: A hidden parameter sent to the bot for deep linking purposes (https://core.telegram.org/bots#deep-linking)
        :type parameter: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = SendBotStartMessage.construct if skip_validation else SendBotStartMessage

        return await self.client.request(
            _constructor(
                bot_user_id=bot_user_id,
                chat_id=chat_id,
                parameter=parameter,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_call_debug_information(
            self,
            call_id: int,
            debug_information: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends debug information for a call
        
        :param call_id: Call identifier
        :type call_id: :class:`int`
        
        :param debug_information: Debug information in application-specific format
        :type debug_information: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SendCallDebugInformation.construct if skip_validation else SendCallDebugInformation

        return await self.client.request(
            _constructor(
                call_id=call_id,
                debug_information=debug_information,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_call_rating(
            self,
            call_id: int,
            rating: int,
            comment: str,
            problems: list[CallProblem],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends a call rating
        
        :param call_id: Call identifier
        :type call_id: :class:`int`
        
        :param rating: Call rating; 1-5
        :type rating: :class:`int`
        
        :param comment: An optional user comment if the rating is less than 5
        :type comment: :class:`str`
        
        :param problems: List of the exact types of problems with the call, specified by the user
        :type problems: :class:`list[CallProblem]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SendCallRating.construct if skip_validation else SendCallRating

        return await self.client.request(
            _constructor(
                call_id=call_id,
                rating=rating,
                comment=comment,
                problems=problems,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_call_signaling_data(
            self,
            call_id: int,
            data: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends call signaling data
        
        :param call_id: Call identifier
        :type call_id: :class:`int`
        
        :param data: The data
        :type data: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SendCallSignalingData.construct if skip_validation else SendCallSignalingData

        return await self.client.request(
            _constructor(
                call_id=call_id,
                data=data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_chat_action(
            self,
            chat_id: int,
            message_thread_id: int,
            action: ChatAction,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends a notification about user activity in a chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param message_thread_id: If not 0, a message thread identifier in which the action was performed
        :type message_thread_id: :class:`int`
        
        :param action: The action description; pass null to cancel the currently active action
        :type action: :class:`ChatAction`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SendChatAction.construct if skip_validation else SendChatAction

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                action=action,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_chat_screenshot_taken_notification(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends a notification about a screenshot taken in a chat. Supported only in private and secret chats
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SendChatScreenshotTakenNotification.construct if skip_validation else SendChatScreenshotTakenNotification

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_custom_request(
            self,
            method: str,
            parameters: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> CustomRequestResult:
        """
        Sends a custom request; for bots only
        
        :param method: The method name
        :type method: :class:`str`
        
        :param parameters: JSON-serialized method parameters
        :type parameters: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.CustomRequestResult`
        """
        _constructor = SendCustomRequest.construct if skip_validation else SendCustomRequest

        return await self.client.request(
            _constructor(
                method=method,
                parameters=parameters,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_email_address_verification_code(
            self,
            email_address: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> EmailAddressAuthenticationCodeInfo:
        """
        Sends a code to verify an email address to be added to a user's Telegram Passport
        
        :param email_address: Email address
        :type email_address: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.EmailAddressAuthenticationCodeInfo`
        """
        _constructor = SendEmailAddressVerificationCode.construct if skip_validation else SendEmailAddressVerificationCode

        return await self.client.request(
            _constructor(
                email_address=email_address,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_inline_query_result_message(
            self,
            chat_id: int,
            message_thread_id: int,
            reply_to_message_id: int,
            options: MessageSendOptions,
            query_id: int,
            result_id: str,
            hide_via_bot: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Sends the result of an inline query as a message. Returns the sent message. Always clears a chat draft message
        
        :param chat_id: Target chat
        :type chat_id: :class:`int`
        
        :param message_thread_id: If not 0, a message thread identifier in which the message will be sent
        :type message_thread_id: :class:`int`
        
        :param reply_to_message_id: Identifier of a replied message; 0 if none
        :type reply_to_message_id: :class:`int`
        
        :param options: Options to be used to send the message; pass null to use default options
        :type options: :class:`MessageSendOptions`
        
        :param query_id: Identifier of the inline query
        :type query_id: :class:`int`
        
        :param result_id: Identifier of the inline result
        :type result_id: :class:`str`
        
        :param hide_via_bot: Pass true to hide the bot, via which the message is sent. Can be used only for bots GetOption("animation_search_bot_username"), GetOption("photo_search_bot_username"), and GetOption("venue_search_bot_username")
        :type hide_via_bot: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = SendInlineQueryResultMessage.construct if skip_validation else SendInlineQueryResultMessage

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                options=options,
                query_id=query_id,
                result_id=result_id,
                hide_via_bot=hide_via_bot,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_message(
            self,
            chat_id: int,
            message_thread_id: int,
            reply_to_message_id: int,
            options: MessageSendOptions,
            reply_markup: ReplyMarkup,
            input_message_content: InputMessageContent,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Sends a message. Returns the sent message
        
        :param chat_id: Target chat
        :type chat_id: :class:`int`
        
        :param message_thread_id: If not 0, a message thread identifier in which the message will be sent
        :type message_thread_id: :class:`int`
        
        :param reply_to_message_id: Identifier of the replied message; 0 if none
        :type reply_to_message_id: :class:`int`
        
        :param options: Options to be used to send the message; pass null to use default options
        :type options: :class:`MessageSendOptions`
        
        :param reply_markup: Markup for replying to the message; pass null if none; for bots only
        :type reply_markup: :class:`ReplyMarkup`
        
        :param input_message_content: The content of the message to be sent
        :type input_message_content: :class:`InputMessageContent`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = SendMessage.construct if skip_validation else SendMessage

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                options=options,
                reply_markup=reply_markup,
                input_message_content=input_message_content,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_message_album(
            self,
            chat_id: int,
            message_thread_id: int,
            reply_to_message_id: int,
            options: MessageSendOptions,
            input_message_contents: list[InputMessageContent],
            only_preview: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Sends 2-10 messages grouped together into an album. Currently, only audio, document, photo and video messages can be grouped into an album. Documents and audio files can be only grouped in an album with messages of the same type. Returns sent messages
        
        :param chat_id: Target chat
        :type chat_id: :class:`int`
        
        :param message_thread_id: If not 0, a message thread identifier in which the messages will be sent
        :type message_thread_id: :class:`int`
        
        :param reply_to_message_id: Identifier of a replied message; 0 if none
        :type reply_to_message_id: :class:`int`
        
        :param options: Options to be used to send the messages; pass null to use default options
        :type options: :class:`MessageSendOptions`
        
        :param input_message_contents: Contents of messages to be sent. At most 10 messages can be added to an album
        :type input_message_contents: :class:`list[InputMessageContent]`
        
        :param only_preview: Pass true to get fake messages instead of actually sending them
        :type only_preview: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """
        _constructor = SendMessageAlbum.construct if skip_validation else SendMessageAlbum

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                options=options,
                input_message_contents=input_message_contents,
                only_preview=only_preview,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_passport_authorization_form(
            self,
            autorization_form_id: int,
            types: list[PassportElementType],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends a Telegram Passport authorization form, effectively sharing data with the service. This method must be called after getPassportAuthorizationFormAvailableElements if some previously available elements are going to be reused
        
        :param autorization_form_id: Authorization form identifier
        :type autorization_form_id: :class:`int`
        
        :param types: Types of Telegram Passport elements chosen by user to complete the authorization form
        :type types: :class:`list[PassportElementType]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SendPassportAuthorizationForm.construct if skip_validation else SendPassportAuthorizationForm

        return await self.client.request(
            _constructor(
                autorization_form_id=autorization_form_id,
                types=types,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_payment_form(
            self,
            chat_id: int,
            message_id: int,
            payment_form_id: int,
            order_info_id: str,
            shipping_option_id: str,
            credentials: InputCredentials,
            tip_amount: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PaymentResult:
        """
        Sends a filled-out payment form to the bot for final verification
        
        :param chat_id: Chat identifier of the Invoice message
        :type chat_id: :class:`int`
        
        :param message_id: Message identifier
        :type message_id: :class:`int`
        
        :param payment_form_id: Payment form identifier returned by getPaymentForm
        :type payment_form_id: :class:`int`
        
        :param order_info_id: Identifier returned by validateOrderInfo, or an empty string
        :type order_info_id: :class:`str`
        
        :param shipping_option_id: Identifier of a chosen shipping option, if applicable
        :type shipping_option_id: :class:`str`
        
        :param credentials: The credentials chosen by user for payment
        :type credentials: :class:`InputCredentials`
        
        :param tip_amount: Chosen by the user amount of tip in the smallest units of the currency
        :type tip_amount: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PaymentResult`
        """
        _constructor = SendPaymentForm.construct if skip_validation else SendPaymentForm

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                payment_form_id=payment_form_id,
                order_info_id=order_info_id,
                shipping_option_id=shipping_option_id,
                credentials=credentials,
                tip_amount=tip_amount,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_phone_number_confirmation_code(
            self,
            hash_: str,
            phone_number: str,
            settings: PhoneNumberAuthenticationSettings,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> AuthenticationCodeInfo:
        """
        Sends phone number confirmation code to handle links of the type internalLinkTypePhoneNumberConfirmation
        
        :param hash_: Hash value from the link
        :type hash_: :class:`str`
        
        :param phone_number: Phone number value from the link
        :type phone_number: :class:`str`
        
        :param settings: Settings for the authentication of the user's phone number; pass null to use default settings
        :type settings: :class:`PhoneNumberAuthenticationSettings`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AuthenticationCodeInfo`
        """
        _constructor = SendPhoneNumberConfirmationCode.construct if skip_validation else SendPhoneNumberConfirmationCode

        return await self.client.request(
            _constructor(
                hash=hash_,
                phone_number=phone_number,
                settings=settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_phone_number_verification_code(
            self,
            phone_number: str,
            settings: PhoneNumberAuthenticationSettings,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> AuthenticationCodeInfo:
        """
        Sends a code to verify a phone number to be added to a user's Telegram Passport
        
        :param phone_number: The phone number of the user, in international format
        :type phone_number: :class:`str`
        
        :param settings: Settings for the authentication of the user's phone number; pass null to use default settings
        :type settings: :class:`PhoneNumberAuthenticationSettings`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AuthenticationCodeInfo`
        """
        _constructor = SendPhoneNumberVerificationCode.construct if skip_validation else SendPhoneNumberVerificationCode

        return await self.client.request(
            _constructor(
                phone_number=phone_number,
                settings=settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_web_app_data(
            self,
            bot_user_id: int,
            button_text: str,
            data: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends data received from a keyboardButtonTypeWebApp web app to a bot
        
        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`int`
        
        :param button_text: Text of the keyboardButtonTypeWebApp button, which opened the web app
        :type button_text: :class:`str`
        
        :param data: Received data
        :type data: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SendWebAppData.construct if skip_validation else SendWebAppData

        return await self.client.request(
            _constructor(
                bot_user_id=bot_user_id,
                button_text=button_text,
                data=data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_account_ttl(
            self,
            ttl: AccountTtl,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the period of inactivity after which the account of the current user will automatically be deleted
        
        :param ttl: New account TTL
        :type ttl: :class:`AccountTtl`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetAccountTtl.construct if skip_validation else SetAccountTtl

        return await self.client.request(
            _constructor(
                ttl=ttl,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_alarm(
            self,
            seconds: float,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Succeeds after a specified amount of time has passed. Can be called before initialization
        
        :param seconds: Number of seconds before the function returns
        :type seconds: :class:`float`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetAlarm.construct if skip_validation else SetAlarm

        return await self.client.request(
            _constructor(
                seconds=seconds,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_authentication_phone_number(
            self,
            phone_number: str,
            settings: PhoneNumberAuthenticationSettings,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the phone number of the user and sends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword
        
        :param phone_number: The phone number of the user, in international format
        :type phone_number: :class:`str`
        
        :param settings: Settings for the authentication of the user's phone number; pass null to use default settings
        :type settings: :class:`PhoneNumberAuthenticationSettings`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetAuthenticationPhoneNumber.construct if skip_validation else SetAuthenticationPhoneNumber

        return await self.client.request(
            _constructor(
                phone_number=phone_number,
                settings=settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_auto_download_settings(
            self,
            settings: AutoDownloadSettings,
            type_: NetworkType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets auto-download settings
        
        :param settings: New user auto-download settings
        :type settings: :class:`AutoDownloadSettings`
        
        :param type_: Type of the network for which the new settings are relevant
        :type type_: :class:`NetworkType`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetAutoDownloadSettings.construct if skip_validation else SetAutoDownloadSettings

        return await self.client.request(
            _constructor(
                settings=settings,
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_background(
            self,
            background: InputBackground,
            type_: BackgroundType,
            for_dark_theme: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Background:
        """
        Changes the background selected by the user; adds background to the list of installed backgrounds
        
        :param background: The input background to use; pass null to create a new filled backgrounds or to remove the current background
        :type background: :class:`InputBackground`
        
        :param type_: Background type; pass null to use the default type of the remote background or to remove the current background
        :type type_: :class:`BackgroundType`
        
        :param for_dark_theme: Pass true if the background is changed for a dark theme
        :type for_dark_theme: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Background`
        """
        _constructor = SetBackground.construct if skip_validation else SetBackground

        return await self.client.request(
            _constructor(
                background=background,
                type=type_,
                for_dark_theme=for_dark_theme,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_bio(
            self,
            bio: typing.Optional[str],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the bio of the current user
        
        :param bio: The new value of the user bio; 0-70 characters without line feeds, defaults to None
        :type bio: :class:`str`, optional
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetBio.construct if skip_validation else SetBio

        return await self.client.request(
            _constructor(
                bio=bio,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_bot_updates_status(
            self,
            pending_update_count: int,
            error_message: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs the server about the number of pending bot updates if they haven't been processed for a long time; for bots only
        
        :param pending_update_count: The number of pending updates
        :type pending_update_count: :class:`int`
        
        :param error_message: The last error message
        :type error_message: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetBotUpdatesStatus.construct if skip_validation else SetBotUpdatesStatus

        return await self.client.request(
            _constructor(
                pending_update_count=pending_update_count,
                error_message=error_message,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_available_reactions(
            self,
            chat_id: int,
            available_reactions: list[str],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes reactions, available in a chat. Available for basic groups, supergroups, and channels. Requires can_change_info administrator right
        
        :param chat_id: Identifier of the chat
        :type chat_id: :class:`int`
        
        :param available_reactions: New list of reactions, available in the chat. All reactions must be active
        :type available_reactions: :class:`list[str]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatAvailableReactions.construct if skip_validation else SetChatAvailableReactions

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                available_reactions=available_reactions,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_client_data(
            self,
            chat_id: int,
            client_data: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes application-specific data associated with a chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param client_data: New value of client_data
        :type client_data: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatClientData.construct if skip_validation else SetChatClientData

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                client_data=client_data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_description(
            self,
            chat_id: int,
            param_description: typing.Optional[str],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes information about a chat. Available for basic groups, supergroups, and channels. Requires can_change_info administrator right
        
        :param chat_id: Identifier of the chat
        :type chat_id: :class:`int`
        
        :param param_description: New chat description; 0-255 characters, defaults to None
        :type param_description: :class:`str`, optional
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatDescription.construct if skip_validation else SetChatDescription

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                param_description=param_description,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_discussion_group(
            self,
            chat_id: int,
            discussion_chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the discussion group of a channel chat; requires can_change_info administrator right in the channel if it is specified
        
        :param chat_id: Identifier of the channel chat. Pass 0 to remove a link from the supergroup passed in the second argument to a linked channel chat (requires can_pin_messages rights in the supergroup)
        :type chat_id: :class:`int`
        
        :param discussion_chat_id: Identifier of a new channel's discussion group. Use 0 to remove the discussion group. Use the method getSuitableDiscussionChats to find all suitable groups. Basic group chats must be first upgraded to supergroup chats. If new chat members don't have access to old messages in the supergroup, then toggleSupergroupIsAllHistoryAvailable must be used first to change that
        :type discussion_chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatDiscussionGroup.construct if skip_validation else SetChatDiscussionGroup

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                discussion_chat_id=discussion_chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_draft_message(
            self,
            chat_id: int,
            message_thread_id: int,
            draft_message: DraftMessage,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the draft message in a chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param message_thread_id: If not 0, a message thread identifier in which the draft was changed
        :type message_thread_id: :class:`int`
        
        :param draft_message: New draft message; pass null to remove the draft
        :type draft_message: :class:`DraftMessage`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatDraftMessage.construct if skip_validation else SetChatDraftMessage

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                draft_message=draft_message,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_location(
            self,
            chat_id: int,
            location: ChatLocation,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the location of a chat. Available only for some location-based supergroups, use supergroupFullInfo.can_set_location to check whether the method is allowed to use
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param location: New location for the chat; must be valid and not null
        :type location: :class:`ChatLocation`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatLocation.construct if skip_validation else SetChatLocation

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                location=location,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_member_status(
            self,
            chat_id: int,
            member_id: MessageSender,
            status: ChatMemberStatus,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the status of a chat member, needs appropriate privileges. This function is currently not suitable for transferring chat ownership; use transferChatOwnership instead. Use addChatMember or banChatMember if some additional parameters needs to be passed
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param member_id: Member identifier. Chats can be only banned and unbanned in supergroups and channels
        :type member_id: :class:`MessageSender`
        
        :param status: The new status of the member in the chat
        :type status: :class:`ChatMemberStatus`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatMemberStatus.construct if skip_validation else SetChatMemberStatus

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                member_id=member_id,
                status=status,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_message_sender(
            self,
            chat_id: int,
            message_sender_id: MessageSender,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Selects a message sender to send messages in a chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param message_sender_id: New message sender for the chat
        :type message_sender_id: :class:`MessageSender`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatMessageSender.construct if skip_validation else SetChatMessageSender

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_sender_id=message_sender_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_message_ttl(
            self,
            chat_id: int,
            ttl: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the message TTL in a chat. Requires can_delete_messages administrator right in basic groups, supergroups and channels Message TTL can't be changed in a chat with the current user (Saved Messages) and the chat 777000 (Telegram).
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param ttl: New TTL value, in seconds; unless the chat is secret, it must be from 0 up to 365 * 86400 and be divisible by 86400
        :type ttl: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatMessageTtl.construct if skip_validation else SetChatMessageTtl

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                ttl=ttl,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_notification_settings(
            self,
            chat_id: int,
            notification_settings: ChatNotificationSettings,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the notification settings of a chat. Notification settings of a chat with the current user (Saved Messages) can't be changed
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param notification_settings: New notification settings for the chat. If the chat is muted for more than 1 week, it is considered to be muted forever
        :type notification_settings: :class:`ChatNotificationSettings`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatNotificationSettings.construct if skip_validation else SetChatNotificationSettings

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                notification_settings=notification_settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_permissions(
            self,
            chat_id: int,
            permissions: ChatPermissions,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the chat members permissions. Supported only for basic groups and supergroups. Requires can_restrict_members administrator right
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param permissions: New non-administrator members permissions in the chat
        :type permissions: :class:`ChatPermissions`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatPermissions.construct if skip_validation else SetChatPermissions

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                permissions=permissions,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_photo(
            self,
            chat_id: int,
            photo: InputChatPhoto,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the photo of a chat. Supported only for basic groups, supergroups and channels. Requires can_change_info administrator right
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param photo: New chat photo; pass null to delete the chat photo
        :type photo: :class:`InputChatPhoto`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatPhoto.construct if skip_validation else SetChatPhoto

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                photo=photo,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_slow_mode_delay(
            self,
            chat_id: int,
            slow_mode_delay: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the slow mode delay of a chat. Available only for supergroups; requires can_restrict_members rights
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param slow_mode_delay: New slow mode delay for the chat, in seconds; must be one of 0, 10, 30, 60, 300, 900, 3600
        :type slow_mode_delay: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatSlowModeDelay.construct if skip_validation else SetChatSlowModeDelay

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                slow_mode_delay=slow_mode_delay,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_theme(
            self,
            chat_id: int,
            theme_name: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the chat theme. Supported only in private and secret chats
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param theme_name: Name of the new chat theme; pass an empty string to return the default theme
        :type theme_name: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatTheme.construct if skip_validation else SetChatTheme

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                theme_name=theme_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_title(
            self,
            chat_id: int,
            title: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the chat title. Supported only for basic groups, supergroups and channels. Requires can_change_info administrator right
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param title: New title of the chat; 1-128 characters
        :type title: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetChatTitle.construct if skip_validation else SetChatTitle

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                title=title,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_commands(
            self,
            scope: BotCommandScope,
            language_code: str,
            commands: list[BotCommand],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the list of commands supported by the bot for the given user scope and language; for bots only
        
        :param scope: The scope to which the commands are relevant; pass null to change commands in the default bot command scope
        :type scope: :class:`BotCommandScope`
        
        :param language_code: A two-letter ISO 639-1 language code. If empty, the commands will be applied to all users from the given scope, for which language there are no dedicated commands
        :type language_code: :class:`str`
        
        :param commands: List of the bot's commands
        :type commands: :class:`list[BotCommand]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetCommands.construct if skip_validation else SetCommands

        return await self.client.request(
            _constructor(
                scope=scope,
                language_code=language_code,
                commands=commands,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_custom_language_pack(
            self,
            info: LanguagePackInfo,
            strings: list[LanguagePackString],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds or changes a custom local language pack to the current localization target
        
        :param info: Information about the language pack. Language pack ID must start with 'X', consist only of English letters, digits and hyphens, and must not exceed 64 characters. Can be called before authorization
        :type info: :class:`LanguagePackInfo`
        
        :param strings: Strings of the new language pack
        :type strings: :class:`list[LanguagePackString]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetCustomLanguagePack.construct if skip_validation else SetCustomLanguagePack

        return await self.client.request(
            _constructor(
                info=info,
                strings=strings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_custom_language_pack_string(
            self,
            language_pack_id: str,
            new_string: LanguagePackString,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds, edits or deletes a string in a custom local language pack. Can be called before authorization
        
        :param language_pack_id: Identifier of a previously added custom local language pack in the current localization target
        :type language_pack_id: :class:`str`
        
        :param new_string: New language pack string
        :type new_string: :class:`LanguagePackString`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetCustomLanguagePackString.construct if skip_validation else SetCustomLanguagePackString

        return await self.client.request(
            _constructor(
                language_pack_id=language_pack_id,
                new_string=new_string,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_database_encryption_key(
            self,
            new_encryption_key: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the database encryption key. Usually the encryption key is never changed and is stored in some OS keychain
        
        :param new_encryption_key: New encryption key
        :type new_encryption_key: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetDatabaseEncryptionKey.construct if skip_validation else SetDatabaseEncryptionKey

        return await self.client.request(
            _constructor(
                new_encryption_key=new_encryption_key,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_default_channel_administrator_rights(
            self,
            default_channel_administrator_rights: typing.Optional[ChatAdministratorRights],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets default administrator rights for adding the bot to channel chats; for bots only
        
        :param default_channel_administrator_rights: Default administrator rights for adding the bot to channels; may be null, defaults to None
        :type default_channel_administrator_rights: :class:`ChatAdministratorRights`, optional
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetDefaultChannelAdministratorRights.construct if skip_validation else SetDefaultChannelAdministratorRights

        return await self.client.request(
            _constructor(
                default_channel_administrator_rights=default_channel_administrator_rights,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_default_group_administrator_rights(
            self,
            default_group_administrator_rights: typing.Optional[ChatAdministratorRights],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets default administrator rights for adding the bot to basic group and supergroup chats; for bots only
        
        :param default_group_administrator_rights: Default administrator rights for adding the bot to basic group and supergroup chats; may be null, defaults to None
        :type default_group_administrator_rights: :class:`ChatAdministratorRights`, optional
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetDefaultGroupAdministratorRights.construct if skip_validation else SetDefaultGroupAdministratorRights

        return await self.client.request(
            _constructor(
                default_group_administrator_rights=default_group_administrator_rights,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_file_generation_progress(
            self,
            generation_id: int,
            expected_size: int,
            local_prefix_size: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs TDLib on a file generation progress
        
        :param generation_id: The identifier of the generation process
        :type generation_id: :class:`int`
        
        :param expected_size: Expected size of the generated file, in bytes; 0 if unknown
        :type expected_size: :class:`int`
        
        :param local_prefix_size: The number of bytes already generated
        :type local_prefix_size: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetFileGenerationProgress.construct if skip_validation else SetFileGenerationProgress

        return await self.client.request(
            _constructor(
                generation_id=generation_id,
                expected_size=expected_size,
                local_prefix_size=local_prefix_size,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_game_score(
            self,
            chat_id: int,
            message_id: int,
            edit_message: bool,
            user_id: int,
            score: int,
            force: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Updates the game score of the specified user in the game; for bots only
        
        :param chat_id: The chat to which the message with the game belongs
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param edit_message: Pass true to edit the game message to include the current scoreboard
        :type edit_message: :class:`bool`
        
        :param user_id: User identifier
        :type user_id: :class:`int`
        
        :param score: The new score
        :type score: :class:`int`
        
        :param force: Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table
        :type force: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """
        _constructor = SetGameScore.construct if skip_validation else SetGameScore

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                edit_message=edit_message,
                user_id=user_id,
                score=score,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_group_call_participant_is_speaking(
            self,
            group_call_id: int,
            audio_source: int,
            is_speaking: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs TDLib that speaking state of a participant of an active group has changed
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param audio_source: Group call participant's synchronization audio source identifier, or 0 for the current user
        :type audio_source: :class:`int`
        
        :param is_speaking: Pass true if the user is speaking
        :type is_speaking: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetGroupCallParticipantIsSpeaking.construct if skip_validation else SetGroupCallParticipantIsSpeaking

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                audio_source=audio_source,
                is_speaking=is_speaking,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_group_call_participant_volume_level(
            self,
            group_call_id: int,
            participant_id: MessageSender,
            volume_level: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes volume level of a participant of an active group call. If the current user can manage the group call, then the participant's volume level will be changed for all users with the default volume level
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param participant_id: Participant identifier
        :type participant_id: :class:`MessageSender`
        
        :param volume_level: New participant's volume level; 1-20000 in hundreds of percents
        :type volume_level: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetGroupCallParticipantVolumeLevel.construct if skip_validation else SetGroupCallParticipantVolumeLevel

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                participant_id=participant_id,
                volume_level=volume_level,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_group_call_title(
            self,
            group_call_id: int,
            title: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets group call title. Requires groupCall.can_be_managed group call flag
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param title: New group call title; 1-64 characters
        :type title: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetGroupCallTitle.construct if skip_validation else SetGroupCallTitle

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                title=title,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_inactive_session_ttl(
            self,
            inactive_session_ttl_days: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the period of inactivity after which sessions will automatically be terminated
        
        :param inactive_session_ttl_days: New number of days of inactivity before sessions will be automatically terminated; 1-366 days
        :type inactive_session_ttl_days: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetInactiveSessionTtl.construct if skip_validation else SetInactiveSessionTtl

        return await self.client.request(
            _constructor(
                inactive_session_ttl_days=inactive_session_ttl_days,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_inline_game_score(
            self,
            inline_message_id: str,
            edit_message: bool,
            user_id: int,
            score: int,
            force: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Updates the game score of the specified user in a game; for bots only
        
        :param inline_message_id: Inline message identifier
        :type inline_message_id: :class:`str`
        
        :param edit_message: Pass true to edit the game message to include the current scoreboard
        :type edit_message: :class:`bool`
        
        :param user_id: User identifier
        :type user_id: :class:`int`
        
        :param score: The new score
        :type score: :class:`int`
        
        :param force: Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table
        :type force: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetInlineGameScore.construct if skip_validation else SetInlineGameScore

        return await self.client.request(
            _constructor(
                inline_message_id=inline_message_id,
                edit_message=edit_message,
                user_id=user_id,
                score=score,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_location(
            self,
            location: Location,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the location of the current user. Needs to be called if GetOption("is_location_visible") is true and location changes for more than 1 kilometer
        
        :param location: The new location of the user
        :type location: :class:`Location`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetLocation.construct if skip_validation else SetLocation

        return await self.client.request(
            _constructor(
                location=location,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_log_stream(
            self,
            log_stream: LogStream,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets new log stream for internal logging of TDLib. Can be called synchronously
        
        :param log_stream: New log stream
        :type log_stream: :class:`LogStream`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetLogStream.construct if skip_validation else SetLogStream

        return await self.client.request(
            _constructor(
                log_stream=log_stream,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_log_tag_verbosity_level(
            self,
            tag: str,
            new_verbosity_level: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the verbosity level for a specified TDLib internal log tag. Can be called synchronously
        
        :param tag: Logging tag to change verbosity level
        :type tag: :class:`str`
        
        :param new_verbosity_level: New verbosity level; 1-1024
        :type new_verbosity_level: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetLogTagVerbosityLevel.construct if skip_validation else SetLogTagVerbosityLevel

        return await self.client.request(
            _constructor(
                tag=tag,
                new_verbosity_level=new_verbosity_level,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_log_verbosity_level(
            self,
            new_verbosity_level: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the verbosity level of the internal logging of TDLib. Can be called synchronously
        
        :param new_verbosity_level: New value of the verbosity level for logging. Value 0 corresponds to fatal errors, value 1 corresponds to errors, value 2 corresponds to warnings and debug warnings, value 3 corresponds to informational, value 4 corresponds to debug, value 5 corresponds to verbose debug, value greater than 5 and up to 1023 can be used to enable even more logging
        :type new_verbosity_level: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetLogVerbosityLevel.construct if skip_validation else SetLogVerbosityLevel

        return await self.client.request(
            _constructor(
                new_verbosity_level=new_verbosity_level,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_menu_button(
            self,
            user_id: int,
            menu_button: BotMenuButton,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets menu button for the given user or for all users; for bots only
        
        :param user_id: Identifier of the user or 0 to set menu button for all users
        :type user_id: :class:`int`
        
        :param menu_button: New menu button
        :type menu_button: :class:`BotMenuButton`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetMenuButton.construct if skip_validation else SetMenuButton

        return await self.client.request(
            _constructor(
                user_id=user_id,
                menu_button=menu_button,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_message_reaction(
            self,
            chat_id: int,
            message_id: int,
            reaction: str,
            is_big: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes chosen reaction for a message
        
        :param chat_id: Identifier of the chat to which the message belongs
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message
        :type message_id: :class:`int`
        
        :param reaction: Text representation of the new chosen reaction. Can be an empty string or the currently chosen non-big reaction to remove the reaction
        :type reaction: :class:`str`
        
        :param is_big: Pass true if the reaction is added with a big animation
        :type is_big: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetMessageReaction.construct if skip_validation else SetMessageReaction

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                reaction=reaction,
                is_big=is_big,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_name(
            self,
            first_name: str,
            last_name: typing.Optional[str],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the first and last name of the current user
        
        :param first_name: The new value of the first name for the current user; 1-64 characters
        :type first_name: :class:`str`
        
        :param last_name: The new value of the optional last name for the current user; 0-64 characters, defaults to None
        :type last_name: :class:`str`, optional
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetName.construct if skip_validation else SetName

        return await self.client.request(
            _constructor(
                first_name=first_name,
                last_name=last_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_network_type(
            self,
            type_: NetworkType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the current network type. Can be called before authorization. Calling this method forces all network connections to reopen, mitigating the delay in switching between different networks, so it must be called whenever the network is changed, even if the network type remains the same. Network type is used to check whether the library can use the network at all and also for collecting detailed network data usage statistics
        
        :param type_: The new network type; pass null to set network type to networkTypeOther
        :type type_: :class:`NetworkType`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetNetworkType.construct if skip_validation else SetNetworkType

        return await self.client.request(
            _constructor(
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_option(
            self,
            name: str,
            value: OptionValue,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the value of an option. (Check the list of available options on https://core.telegram.org/tdlib/options.) Only writable options can be set. Can be called before authorization
        
        :param name: The name of the option
        :type name: :class:`str`
        
        :param value: The new value of the option; pass null to reset option value to a default value
        :type value: :class:`OptionValue`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetOption.construct if skip_validation else SetOption

        return await self.client.request(
            _constructor(
                name=name,
                value=value,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_passport_element(
            self,
            element: InputPassportElement,
            password: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PassportElement:
        """
        Adds an element to the user's Telegram Passport. May return an error with a message "PHONE_VERIFICATION_NEEDED" or "EMAIL_VERIFICATION_NEEDED" if the chosen phone number or the chosen email address must be verified first
        
        :param element: Input Telegram Passport element
        :type element: :class:`InputPassportElement`
        
        :param password: Password of the current user
        :type password: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PassportElement`
        """
        _constructor = SetPassportElement.construct if skip_validation else SetPassportElement

        return await self.client.request(
            _constructor(
                element=element,
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_passport_element_errors(
            self,
            user_id: int,
            errors: list[InputPassportElementError],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs the user that some of the elements in their Telegram Passport contain errors; for bots only. The user will not be able to resend the elements, until the errors are fixed
        
        :param user_id: User identifier
        :type user_id: :class:`int`
        
        :param errors: The errors
        :type errors: :class:`list[InputPassportElementError]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetPassportElementErrors.construct if skip_validation else SetPassportElementErrors

        return await self.client.request(
            _constructor(
                user_id=user_id,
                errors=errors,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_password(
            self,
            old_password: str,
            new_password: str,
            new_hint: str,
            set_recovery_email_address: bool,
            new_recovery_email_address: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PasswordState:
        """
        Changes the password for the current user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed
        
        :param old_password: Previous password of the user
        :type old_password: :class:`str`
        
        :param new_password: New password of the user; may be empty to remove the password
        :type new_password: :class:`str`
        
        :param new_hint: New password hint; may be empty
        :type new_hint: :class:`str`
        
        :param set_recovery_email_address: Pass true to change also the recovery email address
        :type set_recovery_email_address: :class:`bool`
        
        :param new_recovery_email_address: New recovery email address; may be empty
        :type new_recovery_email_address: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PasswordState`
        """
        _constructor = SetPassword.construct if skip_validation else SetPassword

        return await self.client.request(
            _constructor(
                old_password=old_password,
                new_password=new_password,
                new_hint=new_hint,
                set_recovery_email_address=set_recovery_email_address,
                new_recovery_email_address=new_recovery_email_address,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_pinned_chats(
            self,
            chat_list: ChatList,
            chat_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the order of pinned chats
        
        :param chat_list: Chat list in which to change the order of pinned chats
        :type chat_list: :class:`ChatList`
        
        :param chat_ids: The new list of pinned chats
        :type chat_ids: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetPinnedChats.construct if skip_validation else SetPinnedChats

        return await self.client.request(
            _constructor(
                chat_list=chat_list,
                chat_ids=chat_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_poll_answer(
            self,
            chat_id: int,
            message_id: int,
            option_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the user answer to a poll. A poll in quiz mode can be answered only once
        
        :param chat_id: Identifier of the chat to which the poll belongs
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message containing the poll
        :type message_id: :class:`int`
        
        :param option_ids: 0-based identifiers of answer options, chosen by the user. User can choose more than 1 answer option only is the poll allows multiple answers
        :type option_ids: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetPollAnswer.construct if skip_validation else SetPollAnswer

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                option_ids=option_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_profile_photo(
            self,
            photo: InputChatPhoto,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes a profile photo for the current user
        
        :param photo: Profile photo to set
        :type photo: :class:`InputChatPhoto`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetProfilePhoto.construct if skip_validation else SetProfilePhoto

        return await self.client.request(
            _constructor(
                photo=photo,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_recovery_email_address(
            self,
            password: str,
            new_recovery_email_address: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PasswordState:
        """
        Changes the 2-step verification recovery email address of the user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed. If new_recovery_email_address is the same as the email address that is currently set up, this call succeeds immediately and aborts all other requests waiting for an email confirmation
        
        :param password: Password of the current user
        :type password: :class:`str`
        
        :param new_recovery_email_address: New recovery email address
        :type new_recovery_email_address: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PasswordState`
        """
        _constructor = SetRecoveryEmailAddress.construct if skip_validation else SetRecoveryEmailAddress

        return await self.client.request(
            _constructor(
                password=password,
                new_recovery_email_address=new_recovery_email_address,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_scope_notification_settings(
            self,
            scope: NotificationSettingsScope,
            notification_settings: ScopeNotificationSettings,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes notification settings for chats of a given type
        
        :param scope: Types of chats for which to change the notification settings
        :type scope: :class:`NotificationSettingsScope`
        
        :param notification_settings: The new notification settings for the given scope
        :type notification_settings: :class:`ScopeNotificationSettings`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetScopeNotificationSettings.construct if skip_validation else SetScopeNotificationSettings

        return await self.client.request(
            _constructor(
                scope=scope,
                notification_settings=notification_settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_sticker_position_in_set(
            self,
            sticker: InputFile,
            position: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the position of a sticker in the set to which it belongs; for bots only. The sticker set must have been created by the bot
        
        :param sticker: Sticker
        :type sticker: :class:`InputFile`
        
        :param position: New position of the sticker in the set, zero-based
        :type position: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetStickerPositionInSet.construct if skip_validation else SetStickerPositionInSet

        return await self.client.request(
            _constructor(
                sticker=sticker,
                position=position,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_sticker_set_thumbnail(
            self,
            user_id: int,
            name: str,
            thumbnail: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSet:
        """
        Sets a sticker set thumbnail; for bots only. Returns the sticker set
        
        :param user_id: Sticker set owner
        :type user_id: :class:`int`
        
        :param name: Sticker set name
        :type name: :class:`str`
        
        :param thumbnail: Thumbnail to set in PNG, TGS, or WEBM format; pass null to remove the sticker set thumbnail. Thumbnail format must match the format of stickers in the set
        :type thumbnail: :class:`InputFile`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSet`
        """
        _constructor = SetStickerSetThumbnail.construct if skip_validation else SetStickerSetThumbnail

        return await self.client.request(
            _constructor(
                user_id=user_id,
                name=name,
                thumbnail=thumbnail,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_supergroup_sticker_set(
            self,
            supergroup_id: int,
            sticker_set_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the sticker set of a supergroup; requires can_change_info administrator right
        
        :param supergroup_id: Identifier of the supergroup
        :type supergroup_id: :class:`int`
        
        :param sticker_set_id: New value of the supergroup sticker set identifier. Use 0 to remove the supergroup sticker set
        :type sticker_set_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetSupergroupStickerSet.construct if skip_validation else SetSupergroupStickerSet

        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
                sticker_set_id=sticker_set_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_supergroup_username(
            self,
            supergroup_id: int,
            username: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the username of a supergroup or channel, requires owner privileges in the supergroup or channel
        
        :param supergroup_id: Identifier of the supergroup or channel
        :type supergroup_id: :class:`int`
        
        :param username: New value of the username. Use an empty string to remove the username
        :type username: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetSupergroupUsername.construct if skip_validation else SetSupergroupUsername

        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
                username=username,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_tdlib_parameters(
            self,
            parameters: TdlibParameters,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the parameters for TDLib initialization. Works only when the current authorization state is authorizationStateWaitTdlibParameters
        
        :param parameters: Parameters for TDLib initialization
        :type parameters: :class:`TdlibParameters`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetTdlibParameters.construct if skip_validation else SetTdlibParameters

        return await self.client.request(
            _constructor(
                parameters=parameters,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_user_privacy_setting_rules(
            self,
            setting: UserPrivacySetting,
            rules: UserPrivacySettingRules,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes user privacy settings
        
        :param setting: The privacy setting
        :type setting: :class:`UserPrivacySetting`
        
        :param rules: The new privacy rules
        :type rules: :class:`UserPrivacySettingRules`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetUserPrivacySettingRules.construct if skip_validation else SetUserPrivacySettingRules

        return await self.client.request(
            _constructor(
                setting=setting,
                rules=rules,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_username(
            self,
            username: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the username of the current user
        
        :param username: The new value of the username. Use an empty string to remove the username
        :type username: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetUsername.construct if skip_validation else SetUsername

        return await self.client.request(
            _constructor(
                username=username,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_video_chat_default_participant(
            self,
            chat_id: int,
            default_participant_id: MessageSender,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes default participant identifier, on whose behalf a video chat in the chat will be joined
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param default_participant_id: Default group call participant identifier to join the video chats
        :type default_participant_id: :class:`MessageSender`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SetVideoChatDefaultParticipant.construct if skip_validation else SetVideoChatDefaultParticipant

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                default_participant_id=default_participant_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def share_phone_number(
            self,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Shares the phone number of the current user with a mutual contact. Supposed to be called when the user clicks on chatActionBarSharePhoneNumber
        
        :param user_id: Identifier of the user with whom to share the phone number. The user must be a mutual contact
        :type user_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SharePhoneNumber.construct if skip_validation else SharePhoneNumber

        return await self.client.request(
            _constructor(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def start_group_call_recording(
            self,
            group_call_id: int,
            title: typing.Optional[str],
            record_video: bool,
            use_portrait_orientation: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Starts recording of an active group call. Requires groupCall.can_be_managed group call flag
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param title: Group call recording title; 0-64 characters, defaults to None
        :type title: :class:`str`, optional
        
        :param record_video: Pass true to record a video file instead of an audio file
        :type record_video: :class:`bool`
        
        :param use_portrait_orientation: Pass true to use portrait orientation for video instead of landscape one
        :type use_portrait_orientation: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = StartGroupCallRecording.construct if skip_validation else StartGroupCallRecording

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                title=title,
                record_video=record_video,
                use_portrait_orientation=use_portrait_orientation,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def start_group_call_screen_sharing(
            self,
            group_call_id: int,
            audio_source_id: int,
            payload: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Starts screen sharing in a joined group call. Returns join response payload for tgcalls
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param audio_source_id: Screen sharing audio channel synchronization source identifier; received from tgcalls
        :type audio_source_id: :class:`int`
        
        :param payload: Group call join payload; received from tgcalls
        :type payload: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """
        _constructor = StartGroupCallScreenSharing.construct if skip_validation else StartGroupCallScreenSharing

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                audio_source_id=audio_source_id,
                payload=payload,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def start_scheduled_group_call(
            self,
            group_call_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Starts a scheduled group call
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = StartScheduledGroupCall.construct if skip_validation else StartScheduledGroupCall

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def stop_poll(
            self,
            chat_id: int,
            message_id: int,
            reply_markup: ReplyMarkup,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Stops a poll. A poll in a message can be stopped when the message has can_be_edited flag set
        
        :param chat_id: Identifier of the chat to which the poll belongs
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the message containing the poll
        :type message_id: :class:`int`
        
        :param reply_markup: The new message reply markup; pass null if none; for bots only
        :type reply_markup: :class:`ReplyMarkup`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = StopPoll.construct if skip_validation else StopPoll

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def synchronize_language_pack(
            self,
            language_pack_id: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Fetches the latest versions of all strings from a language pack in the current localization target from the server. This method doesn't need to be called explicitly for the current used/base language packs. Can be called before authorization
        
        :param language_pack_id: Language pack identifier
        :type language_pack_id: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = SynchronizeLanguagePack.construct if skip_validation else SynchronizeLanguagePack

        return await self.client.request(
            _constructor(
                language_pack_id=language_pack_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def terminate_all_other_sessions(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Terminates all other sessions of the current user
        
        """
        return await self.client.request(
            TerminateAllOtherSessions(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def terminate_session(
            self,
            session_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Terminates a session of the current user
        
        :param session_id: Session identifier
        :type session_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = TerminateSession.construct if skip_validation else TerminateSession

        return await self.client.request(
            _constructor(
                session_id=session_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_call_bytes(
            self,
            x: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TestBytes:
        """
        Returns the received bytes; for testing only. This is an offline method. Can be called before authorization
        
        :param x: Bytes to return
        :type x: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TestBytes`
        """
        _constructor = TestCallBytes.construct if skip_validation else TestCallBytes

        return await self.client.request(
            _constructor(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_call_empty(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Does nothing; for testing only. This is an offline method. Can be called before authorization
        
        """
        return await self.client.request(
            TestCallEmpty(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_call_string(
            self,
            x: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TestString:
        """
        Returns the received string; for testing only. This is an offline method. Can be called before authorization
        
        :param x: String to return
        :type x: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TestString`
        """
        _constructor = TestCallString.construct if skip_validation else TestCallString

        return await self.client.request(
            _constructor(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_call_vector_int(
            self,
            x: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TestVectorInt:
        """
        Returns the received vector of numbers; for testing only. This is an offline method. Can be called before authorization
        
        :param x: Vector of numbers to return
        :type x: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TestVectorInt`
        """
        _constructor = TestCallVectorInt.construct if skip_validation else TestCallVectorInt

        return await self.client.request(
            _constructor(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_call_vector_int_object(
            self,
            x: list[TestInt],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TestVectorIntObject:
        """
        Returns the received vector of objects containing a number; for testing only. This is an offline method. Can be called before authorization
        
        :param x: Vector of objects to return
        :type x: :class:`list[TestInt]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TestVectorIntObject`
        """
        _constructor = TestCallVectorIntObject.construct if skip_validation else TestCallVectorIntObject

        return await self.client.request(
            _constructor(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_call_vector_string(
            self,
            x: list[str],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TestVectorString:
        """
        Returns the received vector of strings; for testing only. This is an offline method. Can be called before authorization
        
        :param x: Vector of strings to return
        :type x: :class:`list[str]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TestVectorString`
        """
        _constructor = TestCallVectorString.construct if skip_validation else TestCallVectorString

        return await self.client.request(
            _constructor(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_call_vector_string_object(
            self,
            x: list[TestString],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TestVectorStringObject:
        """
        Returns the received vector of objects containing a string; for testing only. This is an offline method. Can be called before authorization
        
        :param x: Vector of objects to return
        :type x: :class:`list[TestString]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TestVectorStringObject`
        """
        _constructor = TestCallVectorStringObject.construct if skip_validation else TestCallVectorStringObject

        return await self.client.request(
            _constructor(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_get_difference(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Forces an updates.getDifference call to the Telegram servers; for testing only
        
        """
        return await self.client.request(
            TestGetDifference(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_network(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Sends a simple network request to the Telegram servers; for testing only. Can be called before authorization
        
        """
        return await self.client.request(
            TestNetwork(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_proxy(
            self,
            server: str,
            port: int,
            type_: ProxyType,
            dc_id: int,
            timeout: float,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends a simple network request to the Telegram servers via proxy; for testing only. Can be called before authorization
        
        :param server: Proxy server IP address
        :type server: :class:`str`
        
        :param port: Proxy server port
        :type port: :class:`int`
        
        :param type_: Proxy type
        :type type_: :class:`ProxyType`
        
        :param dc_id: Identifier of a datacenter with which to test connection
        :type dc_id: :class:`int`
        
        :param timeout: The maximum overall timeout for the request
        :type timeout: :class:`float`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = TestProxy.construct if skip_validation else TestProxy

        return await self.client.request(
            _constructor(
                server=server,
                port=port,
                type=type_,
                dc_id=dc_id,
                timeout=timeout,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_return_error(
            self,
            error: Error,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Error:
        """
        Returns the specified error and ensures that the Error object is used; for testing only. Can be called synchronously
        
        :param error: The error to be returned
        :type error: :class:`Error`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Error`
        """
        _constructor = TestReturnError.construct if skip_validation else TestReturnError

        return await self.client.request(
            _constructor(
                error=error,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_square_int(
            self,
            x: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TestInt:
        """
        Returns the squared received number; for testing only. This is an offline method. Can be called before authorization
        
        :param x: Number to square
        :type x: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TestInt`
        """
        _constructor = TestSquareInt.construct if skip_validation else TestSquareInt

        return await self.client.request(
            _constructor(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_use_update(self, *, request_id: str = None, request_timeout: int = None) -> Update:
        """
        Does nothing and ensures that the Update object is used; for testing only. This is an offline method. Can be called before authorization
        
        """
        return await self.client.request(
            TestUseUpdate(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_all_downloads_are_paused(
            self,
            are_paused: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes pause state of all files in the file download list
        
        :param are_paused: Pass true to pause all downloads; pass false to unpause them
        :type are_paused: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleAllDownloadsArePaused.construct if skip_validation else ToggleAllDownloadsArePaused

        return await self.client.request(
            _constructor(
                are_paused=are_paused,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_bot_is_added_to_attachment_menu(
            self,
            bot_user_id: int,
            is_added: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds or removes a bot to attachment menu. Bot can be added to attachment menu, only if userTypeBot.can_be_added_to_attachment_menu == true
        
        :param bot_user_id: Bot's user identifier
        :type bot_user_id: :class:`int`
        
        :param is_added: Pass true to add the bot to attachment menu; pass false to remove the bot from attachment menu
        :type is_added: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleBotIsAddedToAttachmentMenu.construct if skip_validation else ToggleBotIsAddedToAttachmentMenu

        return await self.client.request(
            _constructor(
                bot_user_id=bot_user_id,
                is_added=is_added,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_chat_default_disable_notification(
            self,
            chat_id: int,
            default_disable_notification: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the value of the default disable_notification parameter, used when a message is sent to a chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param default_disable_notification: New value of default_disable_notification
        :type default_disable_notification: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleChatDefaultDisableNotification.construct if skip_validation else ToggleChatDefaultDisableNotification

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                default_disable_notification=default_disable_notification,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_chat_has_protected_content(
            self,
            chat_id: int,
            has_protected_content: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the ability of users to save, forward, or copy chat content. Supported only for basic groups, supergroups and channels. Requires owner privileges
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param has_protected_content: New value of has_protected_content
        :type has_protected_content: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleChatHasProtectedContent.construct if skip_validation else ToggleChatHasProtectedContent

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                has_protected_content=has_protected_content,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_chat_is_marked_as_unread(
            self,
            chat_id: int,
            is_marked_as_unread: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the marked as unread state of a chat
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param is_marked_as_unread: New value of is_marked_as_unread
        :type is_marked_as_unread: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleChatIsMarkedAsUnread.construct if skip_validation else ToggleChatIsMarkedAsUnread

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                is_marked_as_unread=is_marked_as_unread,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_chat_is_pinned(
            self,
            chat_list: ChatList,
            chat_id: int,
            is_pinned: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the pinned state of a chat. There can be up to GetOption("pinned_chat_count_max")/GetOption("pinned_archived_chat_count_max") pinned non-secret chats and the same number of secret chats in the main/archive chat list
        
        :param chat_list: Chat list in which to change the pinned state of the chat
        :type chat_list: :class:`ChatList`
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param is_pinned: Pass true to pin the chat; pass false to unpin it
        :type is_pinned: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleChatIsPinned.construct if skip_validation else ToggleChatIsPinned

        return await self.client.request(
            _constructor(
                chat_list=chat_list,
                chat_id=chat_id,
                is_pinned=is_pinned,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_download_is_paused(
            self,
            file_id: int,
            is_paused: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes pause state of a file in the file download list
        
        :param file_id: Identifier of the downloaded file
        :type file_id: :class:`int`
        
        :param is_paused: Pass true if the download is paused
        :type is_paused: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleDownloadIsPaused.construct if skip_validation else ToggleDownloadIsPaused

        return await self.client.request(
            _constructor(
                file_id=file_id,
                is_paused=is_paused,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_group_call_enabled_start_notification(
            self,
            group_call_id: int,
            enabled_start_notification: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles whether the current user will receive a notification when the group call will start; scheduled group calls only
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param enabled_start_notification: New value of the enabled_start_notification setting
        :type enabled_start_notification: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleGroupCallEnabledStartNotification.construct if skip_validation else ToggleGroupCallEnabledStartNotification

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                enabled_start_notification=enabled_start_notification,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_group_call_is_my_video_enabled(
            self,
            group_call_id: int,
            is_my_video_enabled: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles whether current user's video is enabled
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param is_my_video_enabled: Pass true if the current user's video is enabled
        :type is_my_video_enabled: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleGroupCallIsMyVideoEnabled.construct if skip_validation else ToggleGroupCallIsMyVideoEnabled

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                is_my_video_enabled=is_my_video_enabled,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_group_call_is_my_video_paused(
            self,
            group_call_id: int,
            is_my_video_paused: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles whether current user's video is paused
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param is_my_video_paused: Pass true if the current user's video is paused
        :type is_my_video_paused: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleGroupCallIsMyVideoPaused.construct if skip_validation else ToggleGroupCallIsMyVideoPaused

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                is_my_video_paused=is_my_video_paused,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_group_call_mute_new_participants(
            self,
            group_call_id: int,
            mute_new_participants: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles whether new participants of a group call can be unmuted only by administrators of the group call. Requires groupCall.can_toggle_mute_new_participants group call flag
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param mute_new_participants: New value of the mute_new_participants setting
        :type mute_new_participants: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleGroupCallMuteNewParticipants.construct if skip_validation else ToggleGroupCallMuteNewParticipants

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                mute_new_participants=mute_new_participants,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_group_call_participant_is_hand_raised(
            self,
            group_call_id: int,
            participant_id: MessageSender,
            is_hand_raised: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles whether a group call participant hand is rased
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param participant_id: Participant identifier
        :type participant_id: :class:`MessageSender`
        
        :param is_hand_raised: Pass true if the user's hand needs to be raised. Only self hand can be raised. Requires groupCall.can_be_managed group call flag to lower other's hand
        :type is_hand_raised: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleGroupCallParticipantIsHandRaised.construct if skip_validation else ToggleGroupCallParticipantIsHandRaised

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                participant_id=participant_id,
                is_hand_raised=is_hand_raised,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_group_call_participant_is_muted(
            self,
            group_call_id: int,
            participant_id: MessageSender,
            is_muted: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles whether a participant of an active group call is muted, unmuted, or allowed to unmute themselves
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param participant_id: Participant identifier
        :type participant_id: :class:`MessageSender`
        
        :param is_muted: Pass true to mute the user; pass false to unmute the them
        :type is_muted: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleGroupCallParticipantIsMuted.construct if skip_validation else ToggleGroupCallParticipantIsMuted

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                participant_id=participant_id,
                is_muted=is_muted,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_group_call_screen_sharing_is_paused(
            self,
            group_call_id: int,
            is_paused: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Pauses or unpauses screen sharing in a joined group call
        
        :param group_call_id: Group call identifier
        :type group_call_id: :class:`int`
        
        :param is_paused: True if screen sharing is paused
        :type is_paused: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleGroupCallScreenSharingIsPaused.construct if skip_validation else ToggleGroupCallScreenSharingIsPaused

        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                is_paused=is_paused,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_message_sender_is_blocked(
            self,
            sender_id: MessageSender,
            is_blocked: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the block state of a message sender. Currently, only users and supergroup chats can be blocked
        
        :param sender_id: Identifier of a message sender to block/unblock
        :type sender_id: :class:`MessageSender`
        
        :param is_blocked: New value of is_blocked
        :type is_blocked: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleMessageSenderIsBlocked.construct if skip_validation else ToggleMessageSenderIsBlocked

        return await self.client.request(
            _constructor(
                sender_id=sender_id,
                is_blocked=is_blocked,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_session_can_accept_calls(
            self,
            session_id: int,
            can_accept_calls: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles whether a session can accept incoming calls
        
        :param session_id: Session identifier
        :type session_id: :class:`int`
        
        :param can_accept_calls: Pass true to allow accepting incoming calls by the session; pass false otherwise
        :type can_accept_calls: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleSessionCanAcceptCalls.construct if skip_validation else ToggleSessionCanAcceptCalls

        return await self.client.request(
            _constructor(
                session_id=session_id,
                can_accept_calls=can_accept_calls,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_session_can_accept_secret_chats(
            self,
            session_id: int,
            can_accept_secret_chats: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles whether a session can accept incoming secret chats
        
        :param session_id: Session identifier
        :type session_id: :class:`int`
        
        :param can_accept_secret_chats: Pass true to allow accepring secret chats by the session; pass false otherwise
        :type can_accept_secret_chats: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleSessionCanAcceptSecretChats.construct if skip_validation else ToggleSessionCanAcceptSecretChats

        return await self.client.request(
            _constructor(
                session_id=session_id,
                can_accept_secret_chats=can_accept_secret_chats,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_is_all_history_available(
            self,
            supergroup_id: int,
            is_all_history_available: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles whether the message history of a supergroup is available to new members; requires can_change_info administrator right
        
        :param supergroup_id: The identifier of the supergroup
        :type supergroup_id: :class:`int`
        
        :param is_all_history_available: The new value of is_all_history_available
        :type is_all_history_available: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleSupergroupIsAllHistoryAvailable.construct if skip_validation else ToggleSupergroupIsAllHistoryAvailable

        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
                is_all_history_available=is_all_history_available,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_is_broadcast_group(
            self,
            supergroup_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Upgrades supergroup to a broadcast group; requires owner privileges in the supergroup
        
        :param supergroup_id: Identifier of the supergroup
        :type supergroup_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleSupergroupIsBroadcastGroup.construct if skip_validation else ToggleSupergroupIsBroadcastGroup

        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_sign_messages(
            self,
            supergroup_id: int,
            sign_messages: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles whether sender signature is added to sent messages in a channel; requires can_change_info administrator right
        
        :param supergroup_id: Identifier of the channel
        :type supergroup_id: :class:`int`
        
        :param sign_messages: New value of sign_messages
        :type sign_messages: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ToggleSupergroupSignMessages.construct if skip_validation else ToggleSupergroupSignMessages

        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
                sign_messages=sign_messages,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def transfer_chat_ownership(
            self,
            chat_id: int,
            user_id: int,
            password: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the owner of a chat. The current user must be a current owner of the chat. Use the method canTransferOwnership to check whether the ownership can be transferred from the current session. Available only for supergroups and channel chats
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param user_id: Identifier of the user to which transfer the ownership. The ownership can't be transferred to a bot or to a deleted user
        :type user_id: :class:`int`
        
        :param password: The password of the current user
        :type password: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = TransferChatOwnership.construct if skip_validation else TransferChatOwnership

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                user_id=user_id,
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def translate_text(
            self,
            text: str,
            from_language_code: str,
            to_language_code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Translates a text to the given language. Returns a 404 error if the translation can't be performed
        
        :param text: Text to translate
        :type text: :class:`str`
        
        :param from_language_code: A two-letter ISO 639-1 language code of the language from which the message is translated. If empty, the language will be detected automatically
        :type from_language_code: :class:`str`
        
        :param to_language_code: A two-letter ISO 639-1 language code of the language to which the message is translated
        :type to_language_code: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """
        _constructor = TranslateText.construct if skip_validation else TranslateText

        return await self.client.request(
            _constructor(
                text=text,
                from_language_code=from_language_code,
                to_language_code=to_language_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def unpin_all_chat_messages(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes all pinned messages from a chat; requires can_pin_messages rights in the group or can_edit_messages rights in the channel
        
        :param chat_id: Identifier of the chat
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = UnpinAllChatMessages.construct if skip_validation else UnpinAllChatMessages

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def unpin_chat_message(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a pinned message from a chat; requires can_pin_messages rights in the group or can_edit_messages rights in the channel
        
        :param chat_id: Identifier of the chat
        :type chat_id: :class:`int`
        
        :param message_id: Identifier of the removed pinned message
        :type message_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = UnpinChatMessage.construct if skip_validation else UnpinChatMessage

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def upgrade_basic_group_chat_to_supergroup_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Creates a new supergroup from an existing basic group and sends a corresponding messageChatUpgradeTo and messageChatUpgradeFrom; requires creator privileges. Deactivates the original basic group
        
        :param chat_id: Identifier of the chat to upgrade
        :type chat_id: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """
        _constructor = UpgradeBasicGroupChatToSupergroupChat.construct if skip_validation else UpgradeBasicGroupChatToSupergroupChat

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def upload_file(
            self,
            file: InputFile,
            file_type: FileType,
            priority: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> File:
        """
        Asynchronously uploads a file to the cloud without sending it in a message. updateFile will be used to notify about upload progress and successful completion of the upload. The file will not have a persistent remote identifier until it will be sent in a message
        
        :param file: File to upload
        :type file: :class:`InputFile`
        
        :param file_type: File type; pass null if unknown
        :type file_type: :class:`FileType`
        
        :param priority: Priority of the upload (1-32). The higher the priority, the earlier the file will be uploaded. If the priorities of two files are equal, then the first one for which uploadFile was called will be uploaded first
        :type priority: :class:`int`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.File`
        """
        _constructor = UploadFile.construct if skip_validation else UploadFile

        return await self.client.request(
            _constructor(
                file=file,
                file_type=file_type,
                priority=priority,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def upload_sticker_file(
            self,
            user_id: int,
            sticker: InputSticker,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> File:
        """
        Uploads a file with a sticker; returns the uploaded file
        
        :param user_id: Sticker file owner; ignored for regular users
        :type user_id: :class:`int`
        
        :param sticker: Sticker file to upload
        :type sticker: :class:`InputSticker`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.File`
        """
        _constructor = UploadStickerFile.construct if skip_validation else UploadStickerFile

        return await self.client.request(
            _constructor(
                user_id=user_id,
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def validate_order_info(
            self,
            chat_id: int,
            message_id: int,
            order_info: OrderInfo,
            allow_save: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ValidatedOrderInfo:
        """
        Validates the order information provided by a user and returns the available shipping options for a flexible invoice
        
        :param chat_id: Chat identifier of the Invoice message
        :type chat_id: :class:`int`
        
        :param message_id: Message identifier
        :type message_id: :class:`int`
        
        :param order_info: The order information, provided by the user; pass null if empty
        :type order_info: :class:`OrderInfo`
        
        :param allow_save: Pass true to save the order information
        :type allow_save: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ValidatedOrderInfo`
        """
        _constructor = ValidateOrderInfo.construct if skip_validation else ValidateOrderInfo

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                order_info=order_info,
                allow_save=allow_save,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def view_messages(
            self,
            chat_id: int,
            message_thread_id: int,
            message_ids: list[int],
            force_read: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs TDLib that messages are being viewed by the user. Sponsored messages must be marked as viewed only when the entire text of the message is shown on the screen (excluding the button). Many useful activities depend on whether the messages are currently being viewed or not (e.g., marking messages as read, incrementing a view counter, updating a view counter, removing deleted messages in supergroups and channels)
        
        :param chat_id: Chat identifier
        :type chat_id: :class:`int`
        
        :param message_thread_id: If not 0, a message thread identifier in which the messages are being viewed
        :type message_thread_id: :class:`int`
        
        :param message_ids: The identifiers of the messages being viewed
        :type message_ids: :class:`list[int]`
        
        :param force_read: Pass true to mark as read the specified messages even the chat is closed
        :type force_read: :class:`bool`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ViewMessages.construct if skip_validation else ViewMessages

        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                message_ids=message_ids,
                force_read=force_read,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def view_trending_sticker_sets(
            self,
            sticker_set_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs the server that some trending sticker sets have been viewed by the user
        
        :param sticker_set_ids: Identifiers of viewed trending sticker sets
        :type sticker_set_ids: :class:`list[int]`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = ViewTrendingStickerSets.construct if skip_validation else ViewTrendingStickerSets

        return await self.client.request(
            _constructor(
                sticker_set_ids=sticker_set_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def write_generated_file_part(
            self,
            generation_id: int,
            offset: int,
            data: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Writes a part of a generated file. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct write to the destination file
        
        :param generation_id: The identifier of the generation process
        :type generation_id: :class:`int`
        
        :param offset: The offset from which to write the data to the file
        :type offset: :class:`int`
        
        :param data: The data to write
        :type data: :class:`str`
        
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """
        _constructor = WriteGeneratedFilePart.construct if skip_validation else WriteGeneratedFilePart

        return await self.client.request(
            _constructor(
                generation_id=generation_id,
                offset=offset,
                data=data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
