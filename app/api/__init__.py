from .physics.electric_explain import router as electric_explain_router
from .physics.student_explain import router as student_explain_router
from .experiment.subject import router as subject_router
from .experiment.bookset import router as bookset_router
from .experiment.book import router as book_router
from .experiment.chapter import router as chapter_router
from .experiment.experiment import router as experiment_router

__all__ = [electric_explain_router, student_explain_router, subject_router, bookset_router, book_router, chapter_router, experiment_router]