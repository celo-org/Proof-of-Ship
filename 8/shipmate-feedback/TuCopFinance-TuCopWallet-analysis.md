# Analysis Report: TuCopFinance/TuCopWallet

Generated: 2025-10-07 00:32:22


## Error

Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_paid_tier_input_token_count, limit: 1000000
Please retry in 37.632466616s. [violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_paid_tier_input_token_count"
  quota_id: "GenerateContentPaidTierInputTokensPerModelPerMinute"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 1000000
}
, links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, retry_delay {
  seconds: 37
}
]
