#ifndef PATOMIC_FORCE_INLINE
#define PATOMIC_FORCE_INLINE

#include <patomic/patomic_config.h>

#if PATOMIC_HAVE_MS_FORCEINLINE
    #define PATOMIC_FORCE_INLINE __forceinline
#endif

#if PATOMIC_HAVE_ALWAYS_INLINE_ATTR
    #define PATOMIC_FORCE_INLINE __attribute__((always_inline))
#endif

#if PATOMIC_HAVE_INLINE_ALWAYS_INLINE_ATTR
    #define PATOMIC_FORCE_INLINE inline __attribute__((always_inline))
#endif

#if PATOMIC_HAVE_GNU_INLINE_ALWAYS_INLINE_ATTR
    #define PATOMIC_FORCE_INLINE __inline__ __attribute__((always_inline))
#endif

#endif  /* !PATOMIC_FORCE_INLINE */
