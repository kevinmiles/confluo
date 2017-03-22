#ifndef UTILS_ASSERTIONS_H_
#define UTILS_ASSERTIONS_H_

#include <cstdlib>
#include <cassert>
#include <exception>
#include <sstream>

#ifndef NDEBUG
#define assert_throw(expr, msg) expr ? (void)0 : (void) (utils::assert::assertion(#expr, __FILE__, __LINE__).get() << msg)
#define assert_fail(expr, msg) expr ? (void)0 : utils::assert::detail::_assert_fail(#expr, __FILE__, __LINE__, ((std::ostringstream) (std::ostringstream() << msg)).str())
#else
#define assert_throw(expr, msg) (void)0
#define assert_fail(expr, msg) (void)0
#endif

namespace utils {

namespace assert {

namespace detail {

static inline void _assert_fail(const char* expr, const char* file, int line,
                                const std::string& msg) {
  std::ostringstream out;
  if (!msg.empty())
    out << msg << ": ";

  std::string expr_str(expr);
  if (expr_str == "false" || expr_str == "FALSE" || expr_str == "0")
    out << " Unreachable code assertion";
  else
    out << " Assertion '" << expr_str << "'";

  out << " failed in file '" << file << "' at line " << line;

  fprintf(stderr, "%s", out.str().c_str());
  std::abort();
}

}

class assertion_failure_exception : public std::exception {
 public:
  assertion_failure_exception(const std::string& msg)
      : msg_(msg.c_str()) {
  }

  virtual const char* what() const throw () {
    return msg_;
  }

 private:
  const char* msg_;
};

class assertion {
 public:
  assertion(const char* expr, const char* file, int line)
      : expr_(expr),
        file_(file),
        line_(line) {
  }

  virtual ~assertion() {
    if (!msg_.str().empty())
      msg_ << ": ";

    std::string expr_str(expr_);
    if (expr_str == "false" || expr_str == "FALSE" || expr_str == "0")
      msg_ << "Unreachable code assertion";
    else
      msg_ << "Assertion '" << expr_str << "'";

    msg_ << " failed, file '" << file_ << "' at line " << line_;
    throw assertion_failure_exception(msg_.str());
  }

  std::ostringstream& get() {
    return msg_;
  }

 private:
  std::ostringstream msg_;
  const char* expr_;
  const char* file_;
  int line_;
};

}

}

#endif /* UTILS_ASSERTIONS_H_ */
